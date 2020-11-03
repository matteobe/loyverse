"""
Trigger ReadTheDocs documentation build and check response for confirmation
"""

import os
import requests

URL = 'https://readthedocs.org/api/v3/projects/loyverse/versions/latest/builds/'
TOKEN = os.getenv('READTHEDOCS_TOKEN')
HEADERS = {
    'Authorization': f'Token {TOKEN}',
    'Content-Length': '0',
    }


def main():
    response = requests.post(URL, headers=HEADERS)
    response = response.json()

    if response['triggered']:
        return 0
    else:
        return 1


if __name__ == '__main__':
    main()
