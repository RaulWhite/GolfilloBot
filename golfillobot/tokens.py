import os
from dotenv import load_dotenv

def get_token():
    if "TEL_BOT_TOKEN" not in os.environ:
        load_dotenv()

    TEL_BOT_TOKEN = os.getenv("TEL_BOT_TOKEN")
    return TEL_BOT_TOKEN
