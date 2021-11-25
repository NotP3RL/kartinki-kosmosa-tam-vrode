import os
from pathlib import Path
import random
import time

from dotenv import load_dotenv
import requests
import telegram

from fetch_spacex import fetch_spacex_last_launch_pictures
from fetch_nasa import fetch_nasa_pictures
from fetch_epic import fetch_epic_pictures


if __name__ == '__main__':
    load_dotenv()
    folder_names = ['spacex', 'nasa', 'epic']
    for folder_name in folder_names
        Path(f'images/{folder_name}').mkdir(parents=True, exist_ok=True)
    nasa_token = os.getenv('NASA_TOKEN')
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    telegram_posting_delay = os.getenv('TELEGRAM_POSTING_DELAY')
    telegram_bot = telegram.Bot(token=telegram_token)
    while True:
        fetch_spacex_last_launch_pictures()
        fetch_nasa_pictures(random.randint(30, 50), nasa_token)
        fetch_epic_pictures(random.randint(5, 10), nasa_token)
        try:
            random_folder_path = f'images/{random.choice(os.listdir("images"))}'
            random_picture = random.choice(os.listdir(random_folder_path))
            with open(f'{random_folder_path}/{random_picture}', 'rb') as picture:
                telegram_bot.send_photo(telegram_chat_id, photo=picture)
            time.sleep(int(telegram_posting_delay))
        except IndexError:
            pass
