"""
Base class sharing common properties and methods that can be reused for all endpoints.
The root url for all Loyverse API requests is https://api.loyverse.com/v1.0.
"""

# TODO: Implement throttling of requests to stay below limits per account (300 requests in 300sec)

import os
import requests
from loyverse.exceptions import AccessTokenMissingError


class Api:
    """
    Base API properties for all endpoints
    """

    def __init__(self, access_token: str = None):
        """
        Api initialization

        Args:
            access_token (str): API access token, can also be defined in the environment variable LOYVERSE_ACCESS_TOKEN
        Notes:
            Initializes the hostname, version and name, as well as the headers containing the access token
        """

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

    def request(self, method: str, path: str, params: dict = None) -> dict:
        """
        API request method

        Args:
            method (str): HTTP method (GET, POST, PUT, PATCH, DELETE)
            path (str): API resource path
            params (dict): query parameters dictionary for passed-in path

        Returns:
            response (dict): parsed JSON response
        """

        if path == '' or path is None:
            url = self.url
        else:
            url = f'{self.url}/{path}'

        if method.lower() == 'get':
            response = self.get_request(url, params)
        else:
            # TODO: Implement PUT, PATCH, DELETE, POST methods
            response = None

        return response

    def get_request(self, url: str, params: dict) -> dict:
        """
        GET method for API requests

        Args:
            url (str): complete url (host + path) for the request
            params (dict): query parameters
        Returns:
            response (dict): parse JSON response
        Notes:
            Function maximizes query limit to maximum available (250) and merges multiple responses if response
            size is larger than maximum (250)
        """

        limit_max = 250
        if params is not None:
            params['limit'] = limit_max

        cursor = True
        response_full = dict()

        while cursor:
            response = requests.get(url, headers=self._header, params=params)
            response.raise_for_status()
            response = response.json()

            if 'cursor' in response:
                params = {
                    'cursor': response['cursor'],
                    'limit': limit_max,
                }
            else:
                cursor = False

            key = list(response.keys())[0]
            if key in response_full:
                response_full[key].extend(response[key])
            else:
                for key in response.keys():
                    response_full[key] = response[key]

        return response_full
