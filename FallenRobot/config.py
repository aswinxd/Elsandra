class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "27589257"
    API_HASH = "0af78b04b48361bc117fa4e06d6d2292"

    

    DATABASE_URL = "postgresql://aswinxd:pbCXc87uQWoR@ep-winter-shadow-a5jlgaos-pooler.us-east-2.aws.neon.tech/elsa?sslmode=require"
    EVENT_LOGS = "-1001535538162"  # Event logs channel to note down important bot level
    MONGO_DB_URI = "mongodb+srv://filetolink:DWPEfBYWs4y1ricL@filetolink.xgmsac5.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mong
    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/7298939991d9f7e46c904.jpg"
    SUPPORT_CHAT = "X1Botchat"  # Your Telegram support group chat username where your users will go and bother you
    TOKEN = "1821123783:AAFJxcZHv-RRsGvhUz5Bi5xN3UljUlARR-8"  # Get bot token from @BotFather on Telegram
    OWNER_ID = "1137799257"  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = [6756452709]  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = False
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
