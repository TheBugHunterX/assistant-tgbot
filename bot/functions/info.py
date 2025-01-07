from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import MessageOriginType
from bot import owner_id
from bot.modules.database.mongodb import MongoDB
from bot.helper.telegram_helper import Message, Button


async def func_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    re_msg = update.message.reply_to_message
    chat_id = " ".join(context.args)
    victim = None

    if re_msg:
        forward_origin = re_msg.forward_origin
        from_user = re_msg.from_user
    
        if forward_origin and forward_origin.type == MessageOriginType.USER:
            victim = forward_origin.sender_user
        
        if from_user and not forward_origin:
            victim = from_user
        
        if not victim:
            await Message.reply_message(update, f"<b>• Full name:</b> <code>{forward_origin.sender_user_name}</code>\n<i>Replied user account is hidden!</i>")
            return
    else:
        victim = user
    
    if chat_id == "db" and re_msg:
        chat_id = victim.id
    
    if not chat_id:
        victim_username = f"@{victim.username}" if victim.username else None
        msg = (
            f"<b>• Full name:</b> <code>{victim.full_name}</code>\n"
            f"<b>  » First name:</b> <code>{victim.first_name}</code>\n"
            f"<b>  » Last name:</b> <code>{victim.last_name}</code>\n"
            f"<b>• Mention:</b> {victim.mention_html()}\n"
            f"<b>• Username:</b> {victim_username}\n"
            f"<b>• ID:</b> <code>{victim.id}</code>\n"
            f"<b>• Lang:</b> <code>{victim.language_code}</code>\n"
            f"<b>• Is bot:</b> <code>{victim.is_bot}</code>\n"
            f"<b>• Is premium:</b> <code>{victim.is_premium}</code>"
        )

        btn_data = {
            "User Profile": f"tg://user?id={victim.id}"
        }

        btn = await Button.ubutton(btn_data) if victim.username else None
        await Message.reply_message(update, msg, btn=btn)
        return
    
    if user.id != owner_id:
        await Message.reply_message(update, "Access denied!")
        return

    find_user = await MongoDB.find_one("users", "user_id", int(chat_id))
    if not find_user:
        await Message.reply_message(update, "User not found!")
        return
    
    entries = [
        "name",
        "user_id",
        "username",
        "mention",
        "lang",
        "echo",
        "active_status"
    ]

    msg = "<b><u>Database info</u></b>\n\n"
    
    for key in entries:
        data = find_user.get(key)
        if key in ["username", "mention"]:
            if key == "username":
                data = f"@{data}" if data else None
                msg += f"<b>{key}</b>: {data}\n"
            else:
                msg += f"<b>{key}</b>: {data}\n"
        else:
            msg += f"<b>{key}</b>: <code>{data}</code>\n"
    
    await Message.reply_message(update, msg)
