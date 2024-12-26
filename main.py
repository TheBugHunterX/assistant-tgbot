import asyncio
import requests
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ChatMemberHandler
)
from bot import bot_token, logger, owner_id, server_url
from bot.helper.telegram_helper import Message
from bot.functions.start import func_start
from bot.functions.help import func_help
from bot.functions.id import func_id
from bot.functions.info import func_info
from bot.functions.broadcast import func_broadcast
from bot.functions.database import func_database
from bot.functions.log import func_log
from bot.functions.shell import func_shell
from bot.functions.sys import func_sys
from bot.functions.filter_all import func_filter_all
from bot.modules.bot_chat_tracker.track_bot_chat import track_bot_chat_act


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
        "help": func_help,
        "id": func_id,
        "info": func_info,
        "broadcast": func_broadcast,
        "database": func_database,
        "log": func_log,
        "shell": func_shell,
        "sys": func_sys
    }

    for command, handler in BOT_COMMANDS.items():
        application.add_handler(CommandHandler(command, handler, block=False))
    
    # filters
    application.add_handler(MessageHandler(filters.ALL, func_filter_all, block=False))
    # Chat Member Handler
    application.add_handler(ChatMemberHandler(track_bot_chat_act, ChatMemberHandler.MY_CHAT_MEMBER)) # for tacking bot/private chat
    # Check Updates
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    async def start_up_work():
        await server_alive()
    
    loop = asyncio.get_event_loop()
    loop.create_task(start_up_work())
    loop.create_task(main())
    loop.run_forever()
