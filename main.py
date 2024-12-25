import asyncio
import requests
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)
from bot import bot_token, logger, owner_id, server_url
from bot.helper.telegram_helper import Message
from bot.functions.start import func_start
from bot.functions.log import func_log
from bot.functions.filter_all import func_filter_all


async def server_alive():
    global server_url
    if not server_url:
        logger.warning("SERVER_URL not provided !!")
        await Message.send_msg(owner_id, "Warning! SERVER_URL not provided!")
        return
    
    while True:
        if server_url[0:4] != "http":
            server_url = f"http://{server_url}"
        try:
            response = requests.get(server_url)
            if response.status_code != 200:
                logger.warning(f"{server_url} is down or unreachable. ❌ - code - {response.status_code}")
        except Exception as e:
            logger.error(f"{server_url} > {e}")
        await asyncio.sleep(180) # 3 min


def main():
    application = ApplicationBuilder().token(bot_token).build()
    # functions
    BOT_COMMANDS = {
        "start": func_start,
        "log": func_log
    }

    for command, handler in BOT_COMMANDS.items():
        application.add_handler(CommandHandler(command, handler, block=False))
    
    # filters
    application.add_handler(MessageHandler(filters.ALL, func_filter_all, block=False))
    # Check Updates
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    async def start_up_work():
        await server_alive()
    
    loop = asyncio.get_event_loop()
    loop.create_task(start_up_work())
    loop.create_task(main())
    loop.run_forever()
