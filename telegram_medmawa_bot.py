import asyncio
import time
import os
import logging
import uuid
import requests
import io
import urllib.request
import json
from fuzzywuzzy import process
from telethon import TelegramClient
from telethon.errors import FloodWaitError, SessionPasswordNeededError, PhoneNumberInvalidError, AuthKeyError
from telethon.tl.functions.contacts import SearchRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from telegram.error import Conflict, NetworkError, TelegramError
from web_scrappers.netnaija import netnaija_web_scrapper
from web_scrappers.tfpdl import tfpdl
from web_scrappers.torrent_1337x import search_torrent1337x

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler('bot_log.txt'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Config
CONFIG_PATH = "configs/config.json"
CONFIG = {}
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, 'r') as f:
        CONFIG = json.load(f)

# Credentials (Environment Variables)
API_ID = int(os.environ.get('API_ID', '22326417'))
API_HASH = os.environ.get('API_HASH', 'c8593ab9cdadfcc2a2d01856a91c7cbb')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo')
PHONE = os.environ.get('PHONE', '+917993643828')
TMDB_API_KEY = os.environ.get('TMDB_API_KEY', '68ee2f30970c38d0d60ebc9800be7451')
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY', 'AIzaSyAnrSzc1SPZet8uAEkNoSAMpmwNhAeBA94')

# Telethon client
client = TelegramClient('medmawa_session', API_ID, API_HASH)

# Cache
ResultsCache = {}
LinksCache = {}
TrailerCache = {}
GROUP_CACHE_FILE = 'groups_cache.json'

# Expanded search keywords
BASE_SEARCH_KEYWORDS = [
    'movies', 'series', 'pdf', 'telugu movies', 'english movies', 'hindi movies',
    'tamil movies', 'web series', 'books', 'medical books', 'movie download',
    'series download', 'telugu series', 'english series', '1080p', '720p',
    'bollywood', 'hollywood', 'south movies', 'movie hub', 'film download',
    'torrent movies', 'new releases', 'latest movies', 'full movie',
    'mdisk movies', 'mdisk bollywood', 'mdisk hollywood', 'mdisk south',
    'movie 1080p', 'series 720p', 'pdf download', 'ebook', 'movie links',
    'telegram movies', 'free movies', 'hd movies', 'south dubbed',
    'telugu dubbed', 'hindi dubbed', 'english dubbed', 'movie torrents',
    'series torrents', 'new movies 2023', 'new movies 2024', 'new movies 2025'
]

# Resources for PDFs
RESOURCES = {
    'robbins pathology': {
        'type': 'book',
        'link': 'https://free.usa1lib.is/book/123457/robbins',
        'note': 'Free PDF',
        'video': 'Robbins Pathology Basics (YouTube)'
    },
    'harrison': {
        'type': 'book',
        'link': 'https://free.usa1lib.is/book/2925676/8e7f5d',
        'note': 'Free PDF',
        'video': 'Harrison’s Internal Medicine (YouTube)'
    }
}

OTP_FILE = "otp.txt"

# Load cached groups
def load_cached_groups():
    if os.path.exists(GROUP_CACHE_FILE):
        with open(GROUP_CACHE_FILE, 'r') as f:
            return json.load(f)
    return []

# Save cached groups
def save_cached_groups(groups):
    with open(GROUP_CACHE_FILE, 'w') as f:
        json.dump(groups, f)

# Utils
def get_file_types(category):
    base_types = ['.mp4', '.mkv', '.avi', '.webm', '.mov']
    extra_types = ['.pdf', '.epub', '.zip', '.rar', '.docx']
    return base_types if category in ['movie', 'series'] else extra_types

def month_converter(date):
    months = {
        '01': 'January', '02': 'February', '03': 'March', '04': 'April',
        '05': 'May', '06': 'June', '07': 'July', '08': 'August',
        '09': 'September', '10': 'October', '11': 'November', '12': 'December'
    }
    start = date[0:4]
    convert = date[5:7]
    end = date[8:]
    converted = months.get(convert, convert)
    return f"{end} {converted} {start}"

async def search(query, category="movie"):
    query = query.replace(' ', '+').lower()
    try:
        url = f'https://api.themoviedb.org/3/search/{category}?api_key={TMDB_API_KEY}&language=en-US&query={query}&page=1&include_adult=false'
        logger.debug(f"TMDB API call: {url}")
        for attempt in range(8):
            try:
                response = requests.get(url, timeout=6)
                logger.debug(f"TMDB response status: {response.status_code}")
                if response.status_code == 429:
                    logger.warning("TMDB rate limit hit, waiting 10 sec...")
                    await asyncio.sleep(10)
                    continue
                if response.status_code != 200:
                    logger.error(f"TMDB API error: Status {response.status_code}, Response: {response.text}")
                    return None
                data = response.json()
                if not data.get("results"):
                    logger.warning(f"No TMDB results for query: {query}, category: {category}")
                    popular_items = ["inception", "the avengers", "hulk", "devara", "breaking bad", "hi nanna", "batman"]
                    corrected = process.extractOne(query.replace('+', ' '), popular_items, score_cutoff=85)
                    if corrected and corrected[1] > 85:
                        logger.info(f"Retrying with corrected query: {corrected[0]}")
                        url = f"https://api.themoviedb.org/3/search/{category}?api_key={TMDB_API_KEY}&query={corrected[0].replace(' ', '+')}"
                        response = requests.get(url, timeout=6)
                        data = response.json()
                results = data.get("results")
                if results:
                    exact_results = [r for r in results if r.get('title', r.get('name', '')).lower() == query.replace('+', ' ')]
                    results = exact_results if exact_results else results
                    logger.info(f"TMDB found {len(results)} results for {query}")
                    return results
                return None
            except requests.exceptions.ConnectTimeout:
                logger.warning(f"TMDB timeout on attempt {attempt + 1}, retrying in {2 ** attempt} sec...")
                await asyncio.sleep(2 ** attempt)
                continue
            except requests.exceptions.RequestException as e:
                logger.error(f"TMDB request error on attempt {attempt + 1}: {str(e)}")
                await asyncio.sleep(2 ** attempt)
                continue
        logger.error("TMDB API failed after 8 retries")
        return None
    except Exception as e:
        logger.error(f"TMDB API exception: {str(e)}")
        return None

def get_movie_type(movie: dict):
    return ['title', 'release_date'] if movie.get('title') else ['name', 'first_air_date']

async def get_raw_image(movie_poster_url: str) -> io.BytesIO | None:
    loop = asyncio.get_running_loop()
    try:
        with urllib.request.urlopen(movie_poster_url, timeout=10) as response:
            file_obj = io.BytesIO(await loop.run_in_executor(None, response.read))
        return file_obj
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        logger.error(f"Poster fetch error: {str(e)}")
        return None

async def get_trailer(query):
    if query in TrailerCache:
        logger.debug(f"Returning cached trailer for {query}")
        return TrailerCache[query]
    try:
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}+trailer&key={YOUTUBE_API_KEY}"
        response = requests.get(url, timeout=6).json()
        if response.get('items'):
            trailer_url = f"https://youtube.com/watch?v={response['items'][0]['id']['videoId']}"
            TrailerCache[query] = trailer_url
            return trailer_url
        return None
    except Exception as e:
        logger.error(f"YouTube API error: {str(e)}")
        return None

async def ensure_client_connection():
    if not client.is_connected():
        logger.debug("Connecting Telethon client...")
        try:
            await client.connect()
            logger.info("Client connected successfully")
        except Exception as e:
            logger.error(f"Failed to connect client: {str(e)}")
            raise
    if not await client.is_user_authorized():
        otp = await get_otp()
        if otp:
            logger.info("Using OTP from otp.txt")
            try:
                await client.start(phone=PHONE, code=otp)
                logger.info("Client authorized with OTP")
            except SessionPasswordNeededError:
                logger.error("2FA password required")
                await client.start(phone=PHONE, password=input("Enter 2FA password: "))
        else:
            logger.warning("No OTP found, requesting new OTP")
            await client.start(phone=PHONE, code_callback=lambda: input("Enter OTP: "))
    return client

async def try_join_group(chat):
    try:
        if hasattr(chat, 'username') and chat.username:
            await client(JoinChannelRequest(chat.username))
            logger.info(f"Joined public group: {chat.username}")
            return True
        return False
    except Exception as e:
        logger.warning(f"Could not join group: {str(e)}")
        return False

# Commands
async def start(update: Update, context):
    logger.info("Received /start command")
    await update.message.reply_text(
        "Rey mawa, welcome to AllInOneBot! Movies, series, PDFs—entire Telegram lo automatic ga search chesi files pampistha. Ex: 'hi nanna', 'batman', 'breaking bad', 'robbins pathology'. /help cheyyi!"
    )

async def help_command(update: Update, context):
    logger.info("Received /help command")
    await update.message.reply_text(
        "**AllInOneBot Usage:**\n- Movies: 'hi nanna', 'batman', 'inception'\n- Series: 'breaking bad'\n- PDFs: 'robbins pathology'\n- OTP save cheyyi in 'otp.txt'!\n/usage for detailed steps."
    )

async def usage(update: Update, context):
    await update.message.reply_text(
        "Step 1: Type the name (ex: 'hi nanna')\n"
        "Step 2: Select Movie, Series, or PDF\n"
        "Step 3: View results, use Next/Prev\n"
        "Step 4: Click Download for links\n"
        "Step 5: Check Telegram groups or external sites"
    )

async def disclaimer(update: Update, context):
    await update.message.reply_text(
        "NOTE: Links from Telegram or external sites. Not responsible for content or legality. Use at own risk!"
    )

async def discover_groups(chat_id, context, query=None):
    logger.info(f"Discovering groups for query: {query or 'general'}")
    try:
        await ensure_client_connection()
        await context.bot.send_message(chat_id=chat_id, text="Telegram lo groups chusthunna...")
        
        # Load cached groups
        groups = load_cached_groups()
        logger.info(f"Loaded {len(groups)} cached groups")
        
        # Dynamic keywords
        search_keywords = BASE_SEARCH_KEYWORDS.copy()
        if query:
            search_keywords.extend([
                query, f"{query} movie", f"{query} series", f"{query} download",
                f"{query} 1080p", f"{query} 720p", f"{query} telugu", f"{query} english",
                f"{query} mp4", f"{query} pdf", f"{query} mdisk", f"{query} torrent",
                f"{query} dubbed", f"{query} hd", f"{query} full movie"
            ])
        
        # Search for new groups
        new_groups = []
        for keyword in search_keywords[:50]:  # Increased to 50 keywords
            for attempt in range(15):  # Increased retries
                try:
                    result = await client(SearchRequest(q=keyword, limit=300))  # Increased to 300 groups
                    for chat in result.chats:
                        if hasattr(chat, 'megagroup') and (chat.megagroup or getattr(chat, 'gigagroup', False)):
                            if chat.id not in groups and chat.id not in new_groups:
                                if await try_join_group(chat):
                                    new_groups.append(chat.id)
                                    logger.debug(f"Joined group ID: {chat.id} for keyword: {keyword}")
                                else:
                                    new_groups.append(chat.id)
                                    logger.debug(f"Found group ID: {chat.id} for keyword: {keyword}")
                    break
                except FloodWaitError as e:
                    logger.warning(f"Flood wait error for {keyword}: {e.seconds} seconds")
                    await context.bot.send_message(chat_id=chat_id, text=f"Rate limit, {e.seconds} sec wait...")
                    await asyncio.sleep(e.seconds)
                except (AuthKeyError, ValueError, Exception) as e:
                    logger.error(f"Telethon search error for {keyword}: {str(e)}")
                    if attempt == 14:
                        logger.error(f"Failed to search {keyword} after 15 attempts")
                        continue
                    await asyncio.sleep(2 ** attempt)
        
        # Combine and deduplicate
        groups = list(set(groups + new_groups))
        logger.info(f"Total groups: {len(groups)}")
        
        # Save to cache
        save_cached_groups(groups)
        
        if not groups:
            logger.warning("No groups found")
            await context.bot.send_message(chat_id=chat_id, text="No groups found ra, external sources chusthunna...")
            return []
        
        return groups
    except Exception as e:
        logger.error(f"Error discovering groups: {str(e)}")
        await context.bot.send_message(chat_id=chat_id, text=f"Error ra: {str(e)}, external sources chusthunna...")
        return []

async def get_otp():
    if os.path.exists(OTP_FILE):
        with open(OTP_FILE, 'r') as f:
            otp = f.read().strip()
        os.remove(OTP_FILE)
        return otp
    return None

async def search_files(query, group_ids, chat_id, context, category):
    file_types = get_file_types(category)
    logger.info(f"Searching files for query: {query}, types: {file_types}, groups: {len(group_ids)}")
    results = []
    await context.bot.send_message(chat_id=chat_id, text=f"Files lo chusthunna: {query}...")
    try:
        await ensure_client_connection()
        for group_id in group_ids[:150]:  # Increased to 150 groups
            try:
                async for message in client.iter_messages(group_id, search=query, limit=200):  # Increased to 200 messages
                    if message.media and hasattr(message.media, 'document'):
                        file_name = "Unknown_File"
                        for attr in message.media.document.attributes:
                            if hasattr(attr, 'file_name'):
                                file_name = attr.file_name
                                break
                        file_size = message.media.document.size / (1024 * 1024)
                        if any(ext in file_name.lower() for ext in file_types):
                            results.append({
                                'chat_id': message.chat_id,
                                'message_id': message.id,
                                'file_name': file_name,
                                'file_size': f"{file_size:.2f} MB"
                            })
                            logger.debug(f"Found file: {file_name} in group {group_id}")
                    if "mdisk.me" in message.text.lower():
                        results.append({
                            'chat_id': message.chat_id,
                            'message_id': message.id,
                            'file_name': f"Mdisk_Link_{query}",
                            'file_size': "Unknown"
                        })
                        logger.debug(f"Found Mdisk link in group {group_id}")
            except FloodWaitError as e:
                await context.bot.send_message(chat_id=chat_id, text=f"Rate limit, {e.seconds} sec wait...")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                logger.error(f"File search error in group {group_id}: {str(e)}")
    except Exception as e:
        logger.error(f"Error searching files: {str(e)}")
        await context.bot.send_message(chat_id=chat_id, text=f"Telegram lo files levu ra, external sources chusthunna...")
    return results

async def get_type(update: Update, context):
    user_input = update.message.text.lower()
    chat_id = update.effective_chat.id
    keyboard = [
        [
            InlineKeyboardButton("Movie", callback_data=f"movie:{user_input}"),
            InlineKeyboardButton("Series", callback_data=f"series:{user_input}"),
            InlineKeyboardButton("PDF", callback_data=f"pdf:{user_input}")
        ]
    ]
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"Is '{user_input}' a Movie, Series, or PDF? Select one ra...",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def search_item(update: Update, context):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id
    category, search_query = query.data.split(":", 1)
    category = category.lower()
    logger.info(f"Searching {category}: {search_query}")

    unique_id = str(uuid.uuid4())[:4]
    keyboard = []

    if category in ['movie', 'series']:
        tmdb_results = await search(search_query, category='movie' if category == 'movie' else 'tv')
        if not tmdb_results:
            await query.message.reply_text(f"No results for '{search_query}' ra, check your internet or try again!")
            keyboard = [[InlineKeyboardButton("Retry", callback_data=f"{category}:{search_query}")]]
            await query.message.reply_text("Click to retry:", reply_markup=InlineKeyboardMarkup(keyboard))
            return

        ResultsCache[chat_id] = {unique_id: tmdb_results}
        result = tmdb_results[0]
        title_key, release_date_key = get_movie_type(result)
        poster_path = result.get("poster_path")
        trailer_url = await get_trailer(search_query)

        genres = []
        if result.get("genre_ids"):
            genre_url = f"https://api.themoviedb.org/3/genre/{category}/list?api_key={TMDB_API_KEY}"
            for attempt in range(3):
                try:
                    response = requests.get(genre_url, timeout=6)
                    genre_data = response.json()
                    genre_map = {g["id"]: g["name"] for g in genre_data.get("genres", [])}
                    genres = [genre_map.get(gid) for gid in result["genre_ids"] if gid in genre_map]
                    break
                except requests.exceptions.RequestException:
                    logger.warning(f"Genre fetch failed, retrying {attempt + 1}...")
                    await asyncio.sleep(2)
                    continue

        caption = (
            f"🎬 Title: {result[title_key]}\n"
            f"🔤 Language: {result['original_language']}\n"
            f"🎯 Released: {month_converter(result[release_date_key]) if result.get(release_date_key) else 'N/A'}\n"
            f"✅ Voted: {result.get('vote_average', 'N/A')}\n"
            f"🎭 Genres: {', '.join(genres) if genres else 'N/A'}\n"
            f"🌐 IMDb: https://www.imdb.com/title/{result.get('imdb_id', 'N/A')}\n"
            f"🎥 Trailer: {trailer_url or 'N/A'}"
        )

        keyboard = [[InlineKeyboardButton("Download", callback_data=f"download:{unique_id}:0")]]
        if len(tmdb_results) > 1:
            keyboard.append([InlineKeyboardButton("Next >>", callback_data=f"page:{unique_id}:1")])

        if poster_path:
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            file_obj = await get_raw_image(poster_url)
            if file_obj:
                await context.bot.send_photo(
                    chat_id=chat_id,
                    photo=file_obj,
                    caption=caption,
                    reply_markup=InlineKeyboardMarkup(keyboard)
                )
            else:
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=caption,
                    reply_markup=InlineKeyboardMarkup(keyboard)
                )
        else:
            await context.bot.send_message(
                chat_id=chat_id,
                text=caption,
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

    group_ids = await discover_groups(chat_id, context, query=search_query)
    if group_ids:
        search_terms = [
            search_query, f"{search_query} {category}", f"{search_query} mp4",
            f"{search_query} 1080p", f"{search_query} 720p", f"{search_query} telugu",
            f"{search_query} english", f"{search_query} mdisk", f"{search_query} dubbed",
            f"{search_query} hd", f"{search_query} torrent", f"{search_query} full movie"
        ]
        all_results = []
        for term in search_terms:
            results = await search_files(term, group_ids, chat_id, context, category)
            all_results.extend(results)
        
        if all_results:
            for result in all_results[:10]:  # Increased to 10 results
                file_link = f"https://t.me/c/{str(result['chat_id']).replace('-100', '')}/{result['message_id']}"
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=f"Found: **{result['file_name']}** ({result['file_size']})\nLink: {file_link}"
                )
        else:
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"Telegram lo files em levu for '{search_query}', external sources chusthunna..."
            )
    
    # Fallback to external scrapers
    external_results = []
    try:
        netnaija_links = await netnaija_web_scrapper(search_query)
        if netnaija_links:
            external_results.extend(netnaija_links)
            logger.debug(f"Found {len(netnaija_links)} Netnaija links")
    except Exception as e:
        logger.error(f"Netnaija scraper error: {str(e)}")
    
    try:
        tfpdl_links = tfpdl(category, search_query)
        async for item in tfpdl_links:
            if isinstance(item, list):
                external_results.extend(item)
                logger.debug(f"Found {len(item)} TFPDL links")
    except Exception as e:
        logger.error(f"TFPDL scraper error: {str(e)}")
    
    try:
        torrent_links = await search_torrent1337x(movie_type=category, title=search_query)
        if torrent_links:
            external_results.extend([{'text': 'Torrent Link', 'url': link} for link in torrent_links[:3]])
            logger.debug(f"Found {len(torrent_links)} Torrent links")
    except Exception as e:
        logger.error(f"Torrent1337x scraper error: {str(e)}")
    
    if external_results:
        keyboard = [[InlineKeyboardButton(link['text'], url=link['url'])] for link in external_results[:5]]
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"External links for '{search_query}':",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"No external links found ra for '{search_query}'. Try another query!"
        )

    if category == 'pdf' and search_query in RESOURCES:
        res = RESOURCES[search_query]
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"**{res['type'].title()}: {search_query}**\nLink: {res['link']}\nNote: {res['note']}\nVideo: {res['video']}"
        )

async def handle_pagination(update: Update, context):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id
    unique_id, page = query.data.split(":")[1:]
    page = int(page)

    cached = ResultsCache.get(chat_id, {}).get(unique_id)
    if not cached or page >= len(cached):
        await query.message.reply_text("No more results ra!")
        return

    result = cached[page]
    title_key, release_date_key = get_movie_type(result)
    trailer_url = await get_trailer(result[title_key])

    category = "movie" if title_key == "title" else "series"
    genres = []
    if result.get("genre_ids"):
        genre_url = f"https://api.themoviedb.org/3/genre/{category}/list?api_key={TMDB_API_KEY}"
        for attempt in range(3):
            try:
                response = requests.get(genre_url, timeout=6)
                genre_data = response.json()
                genre_map = {g["id"]: g["name"] for g in genre_data.get("genres", [])}
                genres = [genre_map.get(gid) for gid in result["genre_ids"] if gid in genre_map]
                break
            except requests.exceptions.RequestException:
                logger.warning(f"Genre fetch failed, retrying {attempt + 1}...")
            await asyncio.sleep(2)
            continue

    caption = (
        f"🎬 Title: {result[title_key]}\n"
        f"🔤 Language: {result['original_language']}\n"
        f"🎯 Released: {month_converter(result[release_date_key]) if result.get(release_date_key) else 'N/A'}\n"
        f"✅ Voted: {result.get('vote_average', 'N/A')}\n"
        f"🎭 Genres: {', '.join(genres) if genres else 'N/A'}\n"
        f"🌐 IMDb: https://www.imdb.com/title/{result.get('imdb_id', 'N/A')}\n"
        f"🎥 Trailer: {trailer_url or 'N/A'}"
    )

    keyboard = [[InlineKeyboardButton("Download", callback_data=f"download:{unique_id}:{page}")]]
    if page > 0:
        keyboard.append([InlineKeyboardButton("<< Prev", callback_data=f"page:{unique_id}:{page-1}")])
    if page < len(cached) - 1:
        keyboard.append([InlineKeyboardButton("Next >>", callback_data=f"page:{unique_id}:{page+1}")])

    if result.get("poster_path"):
        poster_url = f"https://image.tmdb.org/t/p/w500{result['poster_path']}"
        file_obj = await get_raw_image(poster_url)
        if file_obj:
            await query.message.edit_media(
                media=InputMediaPhoto(media=file_obj, caption=caption),
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        else:
            await query.message.edit_text(
                text=caption,
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
    else:
        await query.message.edit_text(
            text=caption,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

async def download_links(update: Update, context):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id
    unique_id, page = query.data.split(":")[1:]
    page = int(page)

    cached = ResultsCache.get(chat_id, {}).get(unique_id)
    if not cached:
        await query.message.reply_text("Search expired, try again!")
        return

    result = cached[page]
    title_key, _ = get_movie_type(result)
    title = result[title_key]
    category = "movie" if title_key == "title" else "series"

    await query.message.reply_text(f"Fetching download links for '{title}'...")
    keyboard = []

    try:
        link3 = await netnaija_web_scrapper(title)
        if link3:
            for link in link3:
                keyboard.append([InlineKeyboardButton(link.get('text', 'Netnaija Link'), url=link.get('url'))])
        else:
            logger.warning(f"No Netnaija links for {title}")
    except Exception as e:
        logger.error(f"Netnaija scraper error: {str(e)}")

    try:
        link5 = tfpdl(category, title)
        async for item in link5:
            if isinstance(item, list):
                for link in item:
                    keyboard.append([InlineKeyboardButton(link.get('title', 'TFPDL Link'), url=link.get('url'))])
            elif isinstance(item, int):
                await query.message.edit_text(text=f"Connecting...{item}%")
            else:
                await query.message.edit_text(text=f"{item}")
    except Exception as e:
        logger.error(f"TFPDL scraper error: {str(e)}")

    try:
        link4 = await search_torrent1337x(movie_type=category, title=title)
        if link4:
            for index, link in enumerate(link4):
                keyboard.append([InlineKeyboardButton("TORRENT LINK", url=link)])
                if index > 3:
                    break
        else:
            logger.warning(f"No Torrent1337x links for {title}")
    except Exception as e:
        logger.error(f"Torrent1337x scraper error: {str(e)}")

    if category == 'pdf':
        keyboard.append([InlineKeyboardButton(f"{title} (USA1Lib)", url=f"https://free.usa1lib.is/s/{title.replace(' ', '+')}")])

    keyboard.append([InlineKeyboardButton("Contact Admin", url="https://t.me/allinonebot")])
    reply_markup = InlineKeyboardMarkup(keyboard)

    if len(keyboard) <= 1:
        await query.message.reply_text("Links Not Found ra! Try another title or check your internet.")
    else:
        await query.message.reply_text("Click to download ra:", reply_markup=InlineKeyboardMarkup(keyboard))

async def handle_message(update: Update, context):
    user_input = update.message.text.lower()
    chat_id = update.effective_chat.id
    logger.info(f"Received message: {user_input}")

    with open("search_log.txt", "a") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {user_input}\n")

    await get_type(update, context)

async def error_handler(update, context):
    logger.error(f"Update {update} caused error: {context.error}")
    if update:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Error ra: {str(context.error)}"
        )

def main():
    logger.info("Starting AllInOneBot...")
    while True:
        try:
            app = Application.builder().token(BOT_TOKEN).build()
            app.add_handler(CommandHandler("start", start))
            app.add_handler(CommandHandler("help", help_command))
            app.add_handler(CommandHandler("usage", usage))
            app.add_handler(CommandHandler("disclaimer", disclaimer))
            app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
            app.add_handler(CallbackQueryHandler(search_item, pattern="^movie:|^series:|^pdf:"))
            app.add_handler(CallbackQueryHandler(download_links, pattern="^download:"))
            app.add_handler(CallbackQueryHandler(handle_pagination, pattern="^page:"))
            app.add_error_handler(error_handler)
            
            logger.info("Bot polling started...")
            app.run_polling(allowed_updates=Update.ALL_TYPES, timeout=60, drop_pending_updates=True)
        except Conflict:
            logger.warning("Conflict error! Retrying after 5 sec...")
            time.sleep(5)
            continue
        except NetworkError as e:
            logger.error(f"Network error: {str(e)}. Retrying in 30 sec...")
            time.sleep(30)
            continue
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}. Restarting in 60 sec...")
            time.sleep(60)
            continue

if __name__ == '__main__':
    main()
