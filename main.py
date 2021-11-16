from datetime import datetime
import os
from urllib.parse import urlparse
from pathlib import Path
import random

from dotenv import load_dotenv
import requests
import telegram

def picture_downloader(url, path, params=''):
    response = requests.get(url, params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    pictures = response.json()['links']['flickr']['original']
    for number, picture in enumerate(pictures):
        picture_downloader(picture, f'images/spacex/spacex{number}.jpg')


def picture_extension(url):
    parsed_url = urlparse(url)
    filepath, filename = os.path.split(parsed_url.path)
    return filename.split(".", 2)[1]


def nasa_picture_downloader(count, token):
    nasa_params = {
        'count': count,
        'api_key': token
    }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=nasa_params)
    response.raise_for_status()
    pictures = response.json()
    for number, picture in enumerate(pictures):
        picture_downloader(picture['hdurl'], f'images/nasa/nasa{number}.{picture_extension(picture["hdurl"])}')


def epic_picture_downloader(token):
    response = requests.get(f'https://api.nasa.gov/EPIC/api/natural/images?api_key={token}')
    response.raise_for_status
    pictures = response.json()[:10]
    epic_params = {
        'api_key': token
    }
    for number, picture in enumerate(pictures):
        picture_date = datetime.strptime(picture['date'], '%Y-%m-%d %H:%M:%S')
        formated_picture_date = picture_date.strftime('%Y/%m/%d')
        picture_downloader(f'https://api.nasa.gov/EPIC/archive/natural/{formated_picture_date}/png/{picture["image"]}.png', f'images/epic/epic{number}.png', epic_params)

if __name__ == '__main__':
    load_dotenv()
    Path("images/spacex").mkdir(parents=True, exist_ok=True)
    Path("images/nasa").mkdir(parents=True, exist_ok=True)
    Path("images/epic").mkdir(parents=True, exist_ok=True)
    nasa_token = os.getenv("NASA_TOKEN")
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
    bot = telegram.Bot(token=telegram_token)
    picture_folders = [
    'spacex',
    'nasa',
    'epic'
    ]
    random_folder = f'images/{random.choice(picture_folders)}'
    random_picture = random.choice(os.listdir(random_folder))
    bot.send_photo(telegram_chat_id, photo=open(f'{random_folder}/{random_picture}', 'rb'))
