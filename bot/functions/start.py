from telegram import Update
from telegram.ext import ContextTypes
from bot import owner_id, welcome_msg
from bot.helper.telegram_helper import Message

async def func_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if user.id == owner_id:
        msg = f"Hi, Boss! Welcome back :) ...\nstart message: <code>{welcome_msg}</code>"
    else:
        msg = welcome_msg
    await Message.reply_msg(update, msg)
