import logging
from telegram import Bot
from bot.alive import alive
from config import CONFIG_VARIABLE

open('log.txt', 'w')

#Enable logging
logging.basicConfig(
    filename="log.txt", format="%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(filename)s - %(message)s", level=logging.INFO
)
#set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
# Disable Werkzeug logging
logging.getLogger('werkzeug').setLevel(logging.ERROR)  # Use logging.CRITICAL to remove it completely

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(filename)s - %(message)s")
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)

logger = logging.getLogger(__name__)

# Config
bot_token = CONFIG_VARIABLE.BOT_TOKEN
owner_id = int(CONFIG_VARIABLE.OWNER_ID)
owner_username = CONFIG_VARIABLE.OWNER_USERNAME
server_url = CONFIG_VARIABLE.SERVER_URL
welcome_msg = CONFIG_VARIABLE.WELCOME_MSG

if not bot_token:
    logger.error("BOT_TOKEN not provided!")
    exit(1)

# Main bot function
bot = Bot(bot_token)

logger.info(
'''
Developed by

 ▄▄▄▄    ██▓  ██████  ██░ ██  ▄▄▄       ██▓    
▓█████▄ ▓██▒▒██    ▒ ▓██░ ██▒▒████▄    ▓██▒    
▒██▒ ▄██▒██▒░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▒██░    
▒██░█▀  ░██░  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒██░    
░▓█  ▀█▓░██░▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░██████▒
░▒▓███▀▒░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░▓  ░
▒░▒   ░  ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░░ ░ ▒  ░
 ░    ░  ▒ ░░  ░  ░   ░  ░░ ░  ░   ▒     ░ ░   
 ░       ░        ░   ░  ░  ░      ░  ░    ░  ░
      ░                                        
                            Library python-telegram-bot
'''
)

# Server breathing
alive()
