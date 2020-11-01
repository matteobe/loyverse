__doc__ = """
Python wrapper for Loyverse API

Copyright: (c) 2020, Matteo Berchier
"""

__title__ = "loyverse"
__version__ = "0.0.1"
__author__ = "Matteo Berchier <maberchier(at)gmail.com>"
__copyright__ = "(c) 2020, Matteo Berchier"

# Load environment variables (if .env file exists)
# TODO: fix this
import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), '.env')
load_dotenv(dotenv_path=env_path)
