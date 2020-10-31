"""
Configuration variables for tests
"""

import os
test_data_dir = os.path.join(os.path.dirname(__file__), 'results')

from .utils import store_json_response
