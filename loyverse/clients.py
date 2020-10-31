"""
API clients classes
"""

from .base import BaseAPI


class LoyverseAPI(BaseAPI):
    """
    General wrapper for all follow-on requests types within Loyverse API
    """

    def __init__(self):
        super().__init__('loyverse', 'https://api.loyverse.com/v1.0')
