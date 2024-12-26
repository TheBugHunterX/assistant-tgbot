from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import MessageOriginType
from bot import owner_id
from bot.helper.telegram_helper import Message


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
                    sent_msg = await Message.send_msg(re_msg.text, e_msg.text_html)
                else:
                    await Message.reply_msg(update, "Error: Forward from None")
        else:
            await Message.reply_msg(update, "Reply to user messages to send the message.")
        
        reaction = "👍" if sent_msg else "👎"
        await Message.react_msg(chat.id, e_msg.id, reaction)
        return

    forwarded_msg = await Message.forward_msg(owner_id, chat.id, e_msg.id)
    if forwarded_msg.forward_origin.type == MessageOriginType.HIDDEN_USER:
        await Message.send_msg(owner_id, f"{user.id}")
        await Message.send_msg(owner_id, f"{user.mention_html()}")
    
    reaction = "👍" if forwarded_msg else "👎"
    await Message.react_msg(chat.id, e_msg.id, reaction)
