import requests

from tools import download_picture
from tools import get_picture_extension


def fetch_nasa_pictures(count, token):
    nasa_params = {
        'count': count,
        'api_key': token
    }
    response = requests.get(
        'https://api.nasa.gov/planetary/apod',
        params=nasa_params
    )
    response.raise_for_status()
    pictures = response.json()
    for number, picture in enumerate(pictures):
        try:
            download_picture(
                picture['hdurl'],
                f'images/nasa/nasa{number}{get_picture_extension(picture["hdurl"])}'
            )
        except KeyError:
            pass
