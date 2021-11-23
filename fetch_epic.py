from datetime import datetime

import requests

from tools import picture_downloader


def fetch_epic_pictures(token):
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
