import os
import json
import logging
import requests
import time
import http.server
import socketserver
import threading
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from requests.exceptions import RequestException

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Environment variables
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
PHONE = os.getenv('PHONE')
TMDB_API_KEY = os.getenv('TMDB_API_KEY')

# Initialize Telethon client
client = TelegramClient('medmawa_session', API_ID, API_HASH)

async def load_cached_groups():
    cache_file = 'groups_cache.json'
    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            logger.error(f"Failed to load {cache_file}: {str(e)}. Resetting to empty list.")
            os.remove(cache_file)
    with open(cache_file, 'w', encoding='utf-8') as f:
        json.dump([], f)
    return []

async def save_cached_groups(groups):
    try:
        with open('groups_cache.json', 'w', encoding='utf-8') as f:
            json.dump(groups, f, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Failed to save groups_cache.json: {str(e)}")

async def discover_groups(chat_id, context, query=None):
    groups = await load_cached_groups()
    known_channels = [
        '@Pirates_of_carabian', '@MoviesFlix', '@PDF_Books',
        '@mdisk_adult_movie_videos_18plus', '@TelegramMovies',
        '@MovieHub4U', '@MoviesNow4U', '@World4uFree'
    ]
    for channel in known_channels:
        try:
            await client(JoinChannelRequest(channel))
            chat = await client.get_entity(channel)
            if chat.id not in groups:
                groups.append(chat.id)
                logger.info(f"Joined channel: {channel} (ID: {chat.id})")
        except Exception as e:
            logger.warning(f"Failed to join {channel}: {str(e)}")
    await save_cached_groups(groups)
    logger.info(f"Total groups: {len(groups)}")
    return groups

async def fetch_tmdb_data(query, content_type, retries=5, delay=2):
    url = f"https://api.themoviedb.org/3/search/{content_type}?api_key={TMDB_API_KEY}&language=en-US&query={query}&page=1&include_adult=false"
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                logger.debug(f"TMDB response status: {response.status_code}")
                return response.json()
            else:
                logger.warning(f"TMDB status {response.status_code} on attempt {attempt}")
        except RequestException as e:
            logger.error(f"TMDB request error on attempt {attempt}: {str(e)}")
            if attempt == retries:
                logger.error("TMDB failed after all retries")
                return None
        time.sleep(delay)
    return None

async def search_files(query, group_ids, chat_id, context, content_type):
    results = []
    for group_id in group_ids:
        try:
            async for message in client.iter_messages(group_id, search=query, limit=10):
                if message.file and (content_type == 'movie' and message.file.ext in ['.mp4', '.mkv', '.avi']):
                    file_size = f"{message.file.size / (1024 * 1024):.2f} MB"
                    results.append({
                        'chat_id': group_id,
                        'message_id': message.id,
                        'file_name': message.file.name or 'Unknown',
                        'file_size': file_size
                    })
        except Exception as e:
            logger.error(f"Error searching group {group_id}: {str(e)}")
    return results

async def netnaija_web_scrapper(query):
    try:
        url = f"https://www.thenetnaija.com/search?t={query}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            logger.debug(f"Successful request to {url}")
            return [{'text': f"Netnaija: {query}", 'url': url}]
        return []
    except Exception as e:
        logger.error(f"Netnaija error: {str(e)}")
        return []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello ra mawa! Send me a movie name or use /quicksearch <name> to find files!")

async def quicksearch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.lower().replace('/quicksearch ', '')
    chat_id = update.effective_chat.id
    logger.info(f"Quicksearch for: {user_input}")
    group_ids = await discover_groups(chat_id, context, query=user_input)
    results = await search_files(user_input, group_ids, chat_id, context, 'movie')
    if results:
        for result in results[:5]:
            file_link = f"https://t.me/c/{str(result['chat_id']).replace('-100', '')}/{result['message_id']}"
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"Found: **{result['file_name']}** ({result['file_size']})\nLink: {file_link}"
            )
    else:
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"No files found ra for '{user_input}' in Telegram, checking external links..."
        )
        external_results = []
        try:
            netnaija_links = await netnaija_web_scrapper(user_input)
            if netnaija_links:
                external_results.extend(netnaija_links)
        except Exception as e:
            logger.error(f"Netnaija error: {str(e)}")
        if external_results:
            keyboard = [[InlineKeyboardButton(link['text'], url=link['url'])] for link in external_results[:5]]
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"External links for '{user_input}':",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        else:
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"No external links found ra for '{user_input}'. Try another query!"
            )

async def search_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.lower()
    chat_id = update.effective_chat.id
    tmdb_data = await fetch_tmdb_data(query, "movie")
    if not tmdb_data or not tmdb_data.get("results"):
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"No movie details found ra for '{query}'. Searching files directly..."
        )
        return await quicksearch(update, context)
    movie = tmdb_data["results"][0]
    title = movie.get("title")
    release_date = movie.get("release_date")
    rating = movie.get("vote_average")
    overview = movie.get("overview")
    message = f"🎬 **{title}**\n📅 Released: {release_date}\n⭐ Rating: {rating}\n📝 Overview: {overview}"
    await context.bot.send_message(chat_id=chat_id, text=message)
    await quicksearch(update, context)

def start_dummy_server():
    PORT = int(os.environ.get("PORT", 8000))
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        logger.info(f"Dummy server running on port {PORT}")
        httpd.serve_forever()

async def main():
    await client.start(phone=PHONE)
    logger.info("Client connected successfully")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quicksearch", quicksearch))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_movie))
    await app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=start_dummy_server, daemon=True).start()
    import asyncio
    asyncio.run(main())