from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "10871792"))
API_HASH = getenv("API_HASH", "6f3f84d0b392900e09b0aed186470890")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/5948678d1dcbc98e11d49.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/5948678d1dcbc98e11d49.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/rev_fxx")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/def_Zoka")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5656828413").split()))


FAILED = "https://graph.org/file/5948678d1dcbc98e11d49.jpg"
