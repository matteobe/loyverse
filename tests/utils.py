"""
Common test utilities
"""

import json
from tests import results_dir


def save_json(response: dict, filename: str) -> None:
    """
    Store the response in dictionary format to a JSON file for later inspection
    Args:
        response (dict): API response in dictionary format (JSON)
        filename (str): name of file to store the response to
    """

    with open(f'{results_dir}/{filename}.json', 'w') as f:
        json.dump(response, f, indent=4, sort_keys=False)

    return None


def error_msg(endpoint: str, msg: str) -> str:
    """
    Format error messages for tests using endpoint:msg structure
    """

    return f'Client.{endpoint}: {msg}.'
