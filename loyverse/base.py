"""
Loyverse Client
"""

import os
import base64
import requests


class BaseAPI:
    """
    General wrapper for all APIs
    """

    def __init__(self, api_name: str, root_url: str):
        self.name = api_name
        self.root_url = root_url

        access_token = f'{self.name.upper()}_ACCESS_TOKEN'
        try:
            self.access_token = os.getenv(access_token)
        except OSError:
            raise OSError(f'No {access_token} environment variable found.')

        self.header = {
            'Authorization': f'Bearer {self.access_token}',
            'apikey': f'{self.access_token}',
        }

    def get(self, path: str, params: dict = None):
        """
        API GET method implementation

        Args:
            path (str): API resource path
            params (dict): query parameters dictionary for passed-in path

        Returns:
            response (dict): un-parsed JSON response
        """

        response = requests.get(f'{self.root_url}/{path}', headers=self.header, params=params)
        response.raise_for_status()

        return response.json()


class BaseOAuth2API:
    """
    General wrapper for all APIs using OAuth2.0
    """

    def __init__(self, api_name: str, root_url: str, oauth_url: str = None):
        self.name = api_name
        self.root_url = root_url
        self.oauth_url = oauth_url
        self.access_token = self.get_access_token()

        self.header = {
            'Authorization': f'Bearer {self.access_token}',
            'apikey': f'{self.access_token}',
        }

    def get_access_token(self):
        """
        Retrieve OAuth2.0 access token and store it in class property
        """

        key = os.getenv(f'{self.name.upper()}_KEY')
        secret = os.getenv(f'{self.name.upper()}_SECRET')

        headers = {
            'Authorization': base64_encode(f'{key}:{secret}')
        }

        params = {
            'grant_type': 'client_credentials'
        }

        response = requests.post(self.oauth_url, headers=headers, params=params)
        response.raise_for_status()
        response = response.json()

        return response['access_token']

    def get(self, path: str, params: dict = None):
        """
        API GET method implementation

        Args:
            path (str): API resource path
            params (dict): query parameters dictionary for passed-in path

        Returns:
            response (dict): un-parsed JSON response
        """

        response = requests.get(f'{self.root_url}/{path}', headers=self.header, params=params)
        response.raise_for_status()

        return response.json()


def base64_encode(message: str) -> str:
    """
    Base64 encoding of string
    """

    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_string = base64_bytes.decode('ascii')

    return base64_string
