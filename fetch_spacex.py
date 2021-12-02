import requests
import random

from tools import download_picture


def fetch_spacex_pictures():
    for number, picture_url in enumerate(get_spacex_random_launch_picture_urls()):
        download_picture(picture_url, f'images/spacex/spacex{number}.jpg')


def get_spacex_random_launch_picture_urls():
    response = requests.get('https://api.spacexdata.com/v4/launches')
    response.raise_for_status()
    random_launch = random.choice(response.json())
    if random_launch['links']['flickr']['original'] != []:
        return random_launch['links']['flickr']['original']
    return get_spacex_random_launch_picture_urls()
