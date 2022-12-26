import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID", 1923471))
    API_HASH = os.environ.get("API_HASH", "fcdc178451cd234e63faefd38895c991")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5424505458:AAGIwqM1MMKB5TToJjaj9ecf25_YSA3ZVNQ")
    OWNER_ID = int(os.environ.get("OWNER_ID", 880087645))
    AUTH_CHANNEL = "-1001695270196"
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Erichdaniken:Erichdaniken@cluster0.vhu3d.mongodb.net/?retryWrites=true&w=majority")
