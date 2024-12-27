from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import MessageOriginType
from bot import owner_id
from bot.helper.telegram_helper import Message, Button


async def func_filter_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user = update.effective_user
    e_msg = update.effective_message
    re_msg = update.message.reply_to_message
    sent_msg = None

    if not e_msg:
        return

    if user.id == owner_id:
        if re_msg:
            if re_msg.forward_origin:
                if re_msg.forward_origin.type != MessageOriginType.HIDDEN_USER:
                    sent_msg = await Message.send_msg(re_msg.forward_origin.sender_user.id, e_msg.text_html)
            else:
                if re_msg.from_user.is_bot:
                    victim_id = re_msg.text.split("#id")[1]
                    sent_msg = await Message.send_msg(victim_id, e_msg.text_html)
                else:
                    await Message.reply_msg(update, "An error occured! Check /log")
        else:
            await Message.reply_msg(update, "Reply to user messages to send the message.")
        
        if re_msg and not sent_msg:
            await Message.reply_msg(update, "Oops, something went wrong. Maybe <code>user id</code> wrong 🤔 or user blocked!!")
        
        reaction = "👍" if sent_msg else "👎"
        await Message.react_msg(chat.id, e_msg.id, reaction)
        return

    forwarded_msg = await Message.forward_msg(owner_id, chat.id, e_msg.id)
    if forwarded_msg.forward_origin.type == MessageOriginType.HIDDEN_USER:
        msg = (
            f"» To answer {user.mention_html()} reply to this message!!\n\n"
            f"<b>User Info:</b>\n"
            f"<b>Name:</b> <code>{user.full_name}</code>\n"
            f"<b>Mention:</b> {user.mention_html()}\n"
            f"<b>Username:</b> {user.name}\n"
            f"<b>ID:</b> <code>{user.id}</code>\n"
            f"<b>Lang:</b> <code>{user.language_code}</code>\n"
            f"#id{user.id}"
        )

        btn_data = {
            "User Profile": f"tg://user?id={user.id}"
        }

        btn = await Button.ubutton(btn_data)
        await Message.send_msg(owner_id, msg, forwarded_msg.id, btn)
    
    reaction = "👍" if forwarded_msg else "👎"
    await Message.react_msg(chat.id, e_msg.id, reaction)
