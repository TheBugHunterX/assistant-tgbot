import asyncio
from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes
from bot import owner_id
from bot.helper.telegram_helper import Message

async def func_log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user = update.effective_user
    e_msg = update.effective_message

    if user.id != owner_id:
        await Message.reply_msg(update, "Access denied!")
        return
    
    if chat.type != "private":
        await Message.reply_msg(update, f"Boss you are in public chat!")
        await asyncio.sleep(3)
        msg_ids = [e_msg.id, e_msg.id + 1]
        await Message.del_msgs(chat.id, msg_ids)
        return
    
    log = open("log.txt", "rb").read()
    date_time = datetime.now()

    await Message.send_doc(user.id, log, "log.txt", date_time.strftime("%d-%m-%Y %H:%M:%S"))
