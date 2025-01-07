from telegram import Update
from telegram.ext import ContextTypes
from bot import owner_id, owner_username
from bot.helper.telegram_helper import Message


async def func_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    msg = (
        f"Hello! I'm the assistant of @{owner_username}.\n"
        f"Feel free to send me a message, and I'll make sure my boss gets it. 😊\n\n"
        f"Interested in creating an assistant like me?\n"
        f"- Check out the <a href='https://github.com/bishalqx980/assistant-tgbot/'>Source Code</a>.\n\n"
        f"Looking for a feature-rich group management bot?\n"
        f"- Take a look at @MissCiri_bot or explore the <a href='https://github.com/bishalqx980/tgbot/'>Source Code</a>.\n\n"
        "<i><b>Note:</b> You can understand whether or not the message was sent by bot reaction!!</i>"
    )

    if user.id == owner_id:
        msg += "\n\nWelcome back Babe 💗"

    await Message.reply_message(update, msg)
