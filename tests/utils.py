"""
Common test utilities
"""

import json
from tests import test_data_dir


def store_json_response(response: dict, filename: str) -> None:
    """
    Store the response in dictionary format to a JSON file for inspection
    """

    with open(f'{test_data_dir}/{filename}.json', 'w') as f:
        json.dump(response, f, indent=4, sort_keys=False)

    return None
