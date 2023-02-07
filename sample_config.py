import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6089522865:AAG0vUsYSBg-BaSfiG1T5E1QTrorjoMDA4U")

    API_ID = int(os.environ.get("API_ID", 17983098))

    API_HASH = os.environ.get("API_HASH", "ee28199396e0925f1f44d945ac174f64")
