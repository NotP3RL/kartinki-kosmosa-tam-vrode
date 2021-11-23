import requests

from tools import picture_downloader
from tools import picture_extension


def fetch_nasa_pictures(count, token):
    nasa_params = {
        'count': count,
        'api_key': token
    }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=nasa_params)
    response.raise_for_status()
    pictures = response.json()
    for number, picture in enumerate(pictures):
        picture_downloader(picture['hdurl'], f'images/nasa/nasa{number}.{picture_extension(picture["hdurl"])}')
