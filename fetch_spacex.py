import requests

from tools import download_picture


def fetch_spacex_last_launch_pictures():
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    pictures = response.json()['links']['flickr']['original']
    for number, picture in enumerate(pictures):
        download_picture(picture, f'images/spacex/spacex{number}.jpg')
