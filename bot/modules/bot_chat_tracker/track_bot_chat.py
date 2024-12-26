from telegram import Update
from telegram.ext import ContextTypes
from bot.modules.database.mongodb import MongoDB
from bot.modules.database.local_database import LOCAL_DATABASE
from bot.modules.bot_chat_tracker.chat_member_status import _chat_member_status


async def track_bot_chat_act(update: Update, context: ContextTypes.DEFAULT_TYPE):
    my_chat_member = update.my_chat_member
    user = my_chat_member.from_user # cause user

    _chk_stat = await _chat_member_status(my_chat_member) # True means user exist and False is not exist
    if not _chk_stat:
        return
    
    bot_exist = _chk_stat

    find_user = await LOCAL_DATABASE.find_one("users", user.id)
    if not find_user:
        find_user = await MongoDB.find_one("users", "user_id", user.id)
        if not find_user:
            data = {
                "user_id": user.id,
                "name": user.full_name,
                "username": user.username,
                "mention": user.mention_html(),
                "lang": user.language_code
            }
            await MongoDB.insert_single_data("users", data)
            await LOCAL_DATABASE.insert_data("users", user.id, data)
    
    if bot_exist:
        await MongoDB.update_db("users", "user_id", user.id, "active_status", True)
    else:
        await MongoDB.update_db("users", "user_id", user.id, "active_status", False)
