#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6761598912:AAHpTerRw0wBW9jJv-DO3WpGTeQeVbnLutc")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20561711"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "be67fa66bf79d732d799ed8fc7d54a16")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002182966979"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "maheshsirop")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1596559467"))

#Port
PORT = os.environ.get("PORT", "8030")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://mongooo1:mongooo1@cluster0.qxhihet.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002208027282"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001348146919"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʙᴀᴋᴋᴀᴀᴀ!! {first}\n\n I am a permanent file Sharing bot and users can access stored messages by using a shareable link given by me.</b>")
try:
    ADMINS=[2052951004]
    for x in (os.environ.get("ADMINS", "2052951004").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Please Join My Channel to use this Bot!\n\n Due to Overload, Only Channel Subscribers can use this Bot!</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• JOIN AND SUPPORT US </b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Bakka ! You Are Not My Master!!"

ADMINS.append(OWNER_ID)
ADMINS.append(2052951004)

LOG_FILE_NAME = "mahesh-file-store-bot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
