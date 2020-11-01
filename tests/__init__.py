"""
Testing functions

Initialization:
* Load environment variables
* Define results directory for storage of API responses
"""

import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=env_path)

results_dir = os.path.join(os.path.dirname(__file__), 'results')
