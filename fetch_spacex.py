import requests

from tools import picture_downloader


def fetch_spacex_last_launch_pictures():
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    pictures = response.json()['links']['flickr']['original']
    for number, picture in enumerate(pictures):
        picture_downloader(picture, f'images/spacex/spacex{number}.jpg')
