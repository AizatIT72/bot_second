import os
import logging
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("BOT_TOKEN")
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv("PORT", default=8000)
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
logging.basicConfig(level=logging.INFO)