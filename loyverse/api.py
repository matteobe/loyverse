"""
Base class sharing common properties and methods that can be reused for all endpoints.
The root url for all Loyverse API requests is https://api.loyverse.com/v1.0.
"""

import os
import requests
from loyverse.exceptions import AccessTokenMissingError


class Api:
    """Base properties for all endpoints"""

    def __init__(self, access_token: str = None):

        self.name = 'loyverse'
        self.version = '1.0'
        self.url = 'https://api.loyverse.com/v1.0'

        if access_token is None:
            try:
                self._access_token = os.getenv('LOYVERSE_ACCESS_TOKEN')
            except AccessTokenMissingError:
                raise AccessTokenMissingError('LOYVERSE_ACCESS_TOKEN not found in environment variables.')
        else:
            self._access_token = access_token

        self._header = {
            'Authorization': f'Bearer {self._access_token}'
        }

    def request(self, method: str, path: str, params: dict = None):
        """
        API request method
        Args:
            method (str): HTTP method (GET, POST, PUT, PATCH, DELETE)
            path (str): API resource path
            params (dict): query parameters dictionary for passed-in path
        Returns:
            response (dict): un-parsed JSON response
        """

        if path == '' or path is None:
            url = self.url
        else:
            url = f'{self.url}/{path}'

        if method.lower() == 'get':
            response = requests.get(url,
                                    headers=self._header,
                                    params=params
                                    )
        # TODO: Implement PUT, PATCH, DELETE, POST methods
        else:
            response = None

        # TODO: Implement different error types
        response.raise_for_status()

        return response.json()
