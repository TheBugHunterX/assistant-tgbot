import time
import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from bot import owner_id
from bot.helper.telegram_helper import Message
from bot.modules.database.mongodb import MongoDB


async def func_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    re_msg = update.message.reply_to_message

    if user.id != owner_id:
        await Message.reply_msg(update, "Access denied!")
        return
    
    if not re_msg:
        await Message.reply_msg(update, "Reply a message to broadcast!")
        return
    
    broadcast_msg = re_msg.text_html or re_msg.caption_html

    users_id = await MongoDB.find("users", "user_id")
    active_status = await MongoDB.find("users", "active_status")

    if len(users_id) == len(active_status):
        combined_list = list(zip(users_id, active_status))
        active_users = []
        for filter_user_id in combined_list:
            if filter_user_id[1] == True:
                active_users.append(filter_user_id[0])
    else:
        await Message.reply_msg(update, f"An error occured!\nuser_id: {len(user_id)} isn't equal to active_status: {len(active_status)} !!")
        return
    
    sent_count, except_count = 0, 0
    notify = await Message.send_msg(user.id, f"Total users: {len(users_id)}\nActive users: {len(active_users)}")
    start_time = time.time()

    for user_id in active_users:
        if re_msg.text_html:
            sent_msg = await Message.send_msg(user_id, broadcast_msg)
        elif re_msg.caption_html:
            sent_msg = await Message.send_img(user_id, re_msg.photo[-1].file_id, broadcast_msg)
        
        if not sent_msg:
            except_count += 1
        else:
            sent_count += 1

        progress = (sent_count + except_count) * 100 / len(active_users)
        await Message.edit_msg(update, f"Total users: {len(users_id)}\nActive users: {len(active_users)}\nSent: {sent_count}\nException occurred: {except_count}\nProgress: {(progress):.2f}%", notify)
        # sleep for 0.5 sec
        await asyncio.sleep(0.5)
    
    end_time = time.time()
    time_took = f"{(end_time - start_time):.2f} sec"
    if (end_time - start_time) > 60:
        time_took = f"{((end_time - start_time) / 60):.2f} min"
    
    await Message.reply_msg(update, f"Broadcast Done!\nTime took: {time_took}")
