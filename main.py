import os
from pathlib import Path
import random
import time

from dotenv import load_dotenv
import requests
import telegram

from fetch_spacex import fetch_spacex_last_launch
from fetch_nasa import nasa_picture_downloader
from fetch_epic import epic_picture_downloader


if __name__ == '__main__':
    load_dotenv()
    Path('images/spacex').mkdir(parents=True, exist_ok=True)
    Path('images/nasa').mkdir(parents=True, exist_ok=True)
    Path('images/epic').mkdir(parents=True, exist_ok=True)
    nasa_token = os.getenv('NASA_TOKEN')
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    telegram_posting_delay = os.getenv('TELEGRAM_POSTING_DELAY')
    telegram_bot = telegram.Bot(token=telegram_token)
    while True:
        fetch_spacex_last_launch()
        nasa_picture_downloader(5, nasa_token)
        epic_picture_downloader(nasa_token)
        try:
            random_folder_path = f'images/{random.choice(os.listdir("images"))}'
            random_picture = random.choice(os.listdir(random_folder_path))
            telegram_bot.send_photo(telegram_chat_id, photo=open(f'{random_folder_path}/{random_picture}', 'rb'))
            time.sleep(int(telegram_posting_delay))
        except IndexError:
            pass
