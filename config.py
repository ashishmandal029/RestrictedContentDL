# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "24871620"))
API_HASH = getenv("API_HASH", "e4195bedc71234a179a3d9ac0cad6401")
BOT_TOKEN = getenv("BOT_TOKEN", "7552955066:AAEoPnh4mpqBbKP_szNCZ1HqA2SHSZW1S58")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5728398903").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ashish:ashish@cluster0.2pxqhuu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1001954419405")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001954419405"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
