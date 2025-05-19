from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

LOG_GROUP_ID = -1002468318697  # Replace with your actual log group ID

OWNER_ID = int(getenv("OWNER_ID", 7142782067))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/MrGhostsx2")
