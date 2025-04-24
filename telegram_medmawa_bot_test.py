import asyncio
import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.error import Conflict, NetworkError, TelegramError

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Your credentials
BOT_TOKEN = '7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs'

# /start command
async def start(update, context):
    logger.info("Received /start command")
    try:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Rey mawa, MedMawaBot started ra! Test successful. Full bot soon. Try /help."
        )
    except Exception as e:
        logger.error(f"Error in start command: {str(e)}")
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Error ra: {str(e)}"
        )

# /help command
async def help_command(update, context):
    logger.info("Received /help command")
    try:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Rey mawa, MedMawaBot here ra! Use /start to begin, more features coming!"
        )
    except Exception as e:
        logger.error(f"Error in help command: {str(e)}")
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Error ra: {str(e)}"
        )

# Error handler
async def error_handler(update, context):
    logger.error(f"Update {update} caused error: {context.error}")
    if update:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Error ra: {str(context.error)}"
        )

# Bot setup
def main():
    logger.info("Starting MedMawaBot...")
    try:
        app = Application.builder().token(BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("help", help_command))
        app.add_error_handler(error_handler)
        
        logger.info("Bot polling started...")
        app.run_polling()
    except Conflict:
        logger.warning("Conflict error! Retrying after 5 sec...")
        time.sleep(5)
        app.run_polling()
    except NetworkError as e:
        logger.error(f"Network error: {str(e)}")
        raise
    except TelegramError as e:
        logger.error(f"Telegram error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"General error: {str(e)}")
        raise
    finally:
        logger.info("Shutting down MedMawaBot...")

if __name__ == '__main__':
    main()