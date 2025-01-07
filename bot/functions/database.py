from telegram import Update
from telegram.ext import ContextTypes
from bot import owner_id
from bot.modules.database.mongodb import MongoDB
from bot.helper.telegram_helper import Message


async def func_database(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if user.id != owner_id:
        await Message.reply_message(update, "Access denied!")
        return
    
    db = await MongoDB.info_db()
    msg = "<b>⋰⋰⋰⋰⋰⋰⋰⋰⋰⋰</b>\n"
    for info in db:
        msg += (
            f"<b>Name</b>: <code>{info[0]}</code>\n"
            f"<b>Count</b>: <code>{info[1]}</code>\n"
            f"<b>Size</b>: <code>{info[2]}</code>\n"
            f"<b>A. size</b>: <code>{info[3]}</code>\n"
            f"<b>⋰⋰⋰⋰⋰⋰⋰⋰⋰⋰</b>\n"
        )
    
    active_status = await MongoDB.find("users", "active_status")
    active_users = active_status.count(True)
    inactive_users = active_status.count(False)
    await Message.reply_message(update, f"{msg}<b>Active users</b>: <code>{active_users}</code>\n<b>Inactive users</b>: <code>{inactive_users}</code>")
