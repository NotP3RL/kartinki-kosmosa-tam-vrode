import os
from urllib.parse import urlparse
from urllib.parse import unquote

import requests


def download_picture(url, path, params=''):
    response = requests.get(url, params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_picture_extension(url):
    parsed_url = urlparse(url)
    return unquote(os.path.splitext(parsed_url.path)[1])
