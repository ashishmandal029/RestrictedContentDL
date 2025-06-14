import asyncio
import logging
import time
from pyrogram import Client
from pyrogram.enums import ParseMode
from telethon.sync import TelegramClient
from motor.motor_asyncio import AsyncIOMotorClient
from config import API_ID, API_HASH, BOT_TOKEN, STRING, MONGO_DB, DEFAULT_SESSION

# Custom logging filter to limit logged messages
class CustomFilter(logging.Filter):
    def filter(self, record):
        return record.name == "snigdha" and record.msg in [
            "Creating Telethon Bot Client From BOT_TOKEN",
            "Telethon Bot Client Created Successfully",
            "Creating Pyro Bot Client From BOT_TOKEN",
            "Pyro Bot Client Created Successfully",
            "Creating Mongo Client From MONGO_DB",
            "Mongo Client Created Successfully",
            "RestrictedContentDL Successfully Started 💥"
        ]

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.addFilter(CustomFilter())
logging.getLogger().handlers = [handler]
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

# Set up event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# Record bot start time
botStartTime = time.time()

# Initialize Telethon client
logger.info("Creating Telethon Bot Client From BOT_TOKEN")
sex = TelegramClient('sexrepo', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
logger.info("Telethon Bot Client Created Successfully")

# Initialize Pyrogram client
logger.info("Creating Pyro Bot Client From BOT_TOKEN")
app = Client(
    "pyrobot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=50,
    parse_mode=ParseMode.MARKDOWN
)

# Initialize optional Pyrogram clients
if STRING:
    pro = Client("ggbot", api_id=API_ID, api_hash=API_HASH, session_string=STRING)
else:
    pro = None

if DEFAULT_SESSION:
    userrbot = Client("userrbot", api_id=API_ID, api_hash=API_HASH, session_string=DEFAULT_SESSION)
else:
    userrbot = None

# Initialize another Telethon client
telethon_client = TelegramClient('telethon_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
logger.info("Pyro Bot Client Created Successfully")

# Initialize MongoDB client
logger.info("Creating Mongo Client From MONGO_DB")
tclient = AsyncIOMotorClient(MONGO_DB)
tdb = tclient["telegram_bot"]
token = tdb["tokens"]
logger.info("Mongo Client Created Successfully")

async def create_ttl_index():
    # Create TTL index for automatic document expiration
    await token.create_index("expires_at", expireAfterSeconds=0)

async def setup_database():
    # Set up database configuration
    await create_ttl_index()

async def restrict_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    # Set up database
    await setup_database()
    
    # Start Pyrogram client and get bot info
    await app.start()
    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    BOT_NAME = f"{getme.first_name} {getme.last_name}" if getme.last_name else getme.first_name
    
    # Start optional clients if available
    if pro:
        await pro.start()
    if userrbot:
        await userrbot.start()
    
    logger.info("RestrictedContentDL Successfully Started 💥")

# Run the bot
loop.run_until_complete(restrict_bot())