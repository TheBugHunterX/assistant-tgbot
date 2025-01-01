from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import MessageOriginType
from bot import owner_id
from bot.helper.telegram_helper import Message, Button


async def assistant_go(victim_id, e_msg):
    text = e_msg.text_html
    photo = e_msg.photo
    audio = e_msg.audio
    video = e_msg.video
    document = e_msg.document
    caption = e_msg.caption_html
    sent_msg = None

    # in future update
    # voice = e_msg.voice
    # video_note = e_msg.video_note

    if text:
        sent_msg = await Message.send_msg(victim_id, text)
    elif photo:
        sent_msg = await Message.send_img(victim_id, photo[-1].file_id, caption)
    elif audio:
        sent_msg = await Message.send_audio(victim_id, audio.file_id, audio.file_name, caption)
    elif video:
        sent_msg = await Message.send_vid(victim_id, video.file_id, caption=caption)
    elif document:
        sent_msg = await Message.send_doc(victim_id, document.file_id, document.file_name, caption)
    
    return sent_msg


async def func_filter_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user = update.effective_user
    e_msg = update.effective_message
    re_msg = update.message.reply_to_message
    sent_msg = None
    victim_id = None

    if user.id == owner_id:
        # this section is for owner logic
        if not re_msg:
            await Message.reply_msg(update, "Reply to user messages to send the message.")
            return
        
        # getting victim_id
        if re_msg.forward_origin:
            # if victim account isn't hidden
            if re_msg.forward_origin.type != MessageOriginType.HIDDEN_USER:
                victim_id = re_msg.forward_origin.sender_user.id
        else:
            # if victim is hidden
            if re_msg.from_user.is_bot:
                check_msg = re_msg.text.split("#id")
                if len(check_msg) >= 2:
                    victim_id = check_msg[1]
                else:
                    await Message.reply_msg(update, "You have replied the wrong message.")
                    return
            else:
                await Message.reply_msg(update, "Reply to user messages to send the message.")
                return
        
        if not victim_id:
            await Message.reply_msg(update, "Error: victim_id not found!")
            return
        
        # check message type and send message to victim
        sent_msg = await assistant_go(victim_id, e_msg)
        if not sent_msg:
            await Message.reply_msg(update, "Oops, something went wrong. Maybe <code>user id</code> wrong 🤔 or user blocked!!")
            return
        
        reaction = "❤" if sent_msg else "👎"
        await Message.react_msg(chat.id, e_msg.id, reaction)
    else:
        # this section is for user logic
        forwarded_msg = await Message.forward_msg(owner_id, chat.id, e_msg.id)
        if e_msg.audio or forwarded_msg.forward_origin.type == MessageOriginType.HIDDEN_USER:
            # if user is hidden or its audio file
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
            
            btn = await Button.ubutton({"User Profile": f"tg://user?id={user.id}"}) if user.username else None
            await Message.send_msg(owner_id, msg, forwarded_msg.id, btn)
        
        reaction = "❤" if forwarded_msg else "👎"
        await Message.react_msg(chat.id, e_msg.id, reaction)
