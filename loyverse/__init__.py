__doc__ = """
Python wrapper for Loyverse API

Copyright: (c) 2020, Matteo Berchier
"""

__title__ = "loyverse"
__version__ = "0.0.1"
__author__ = "Matteo Berchier <maberchier(at)gmail.com>"
__copyright__ = "(c) 2020, Matteo Berchier"

# Load environment variables (if .env file exists)
import os
from dotenv import load_dotenv
from pathlib import Path
env_path = f"{Path('.')}/.env"
load_dotenv(dotenv_path=env_path)


from .receipts import ReceiptsAPI
from .customers import CustomersAPI
