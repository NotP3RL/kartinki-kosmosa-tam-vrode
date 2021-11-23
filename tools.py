import os
from urllib.parse import urlparse

import requests


def picture_downloader(url, path, params=''):
    response = requests.get(url, params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def picture_extension(url):
    parsed_url = urlparse(url)
    filepath, filename = os.path.split(parsed_url.path)
    return filename.split(".", 2)[1]
