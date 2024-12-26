from telegram import Update
from telegram.ext import ContextTypes
from bot.helper.telegram_helper import Message

async def func_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "/start - start the bot\n"
        "/id - get user/chat id\n"
        "/info - get user info\n"
        "/help - get this message :)\n\n"
        "Bot owner commands -\n\n"
        "/sys - get system info\n"
        "/broadcast - broadcast message to all user\n"
        "/database - get database info\n"
        "/log - for development/finding any error/bug\n"
        "/shell - use system shell\n"
    )

    await Message.reply_msg(update, msg)