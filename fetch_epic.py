from datetime import datetime

import requests

from tools import download_picture


def fetch_epic_pictures(count, token):
    epic_params = {
        'api_key': token
    }
    response = requests.get(
        'https://api.nasa.gov/EPIC/api/natural/images',
        params=epic_params
    )
    response.raise_for_status
    pictures = response.json()[:count]
    for number, picture in enumerate(pictures):
        picture_date = datetime.strptime(picture['date'], '%Y-%m-%d %H:%M:%S')
        formated_picture_date = picture_date.strftime('%Y/%m/%d')
        picture_url = f'https://api.nasa.gov/EPIC/archive/natural/{formated_picture_date}/png/{picture["image"]}.png'
        picture_path = f'images/epic/epic{number}.png'
        download_picture(picture_url, picture_path, epic_params)
