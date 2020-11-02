"""
The Client class encapsulates the endpoints of the Loyverse API and provides a single point of initialization for
API requests.

The Client class exposes the following end-points

* receipts
* customers
"""

from loyverse.api import Api


class Client:
    """Loyverse API client

    Args:
        access_token (str): Access token string to be used to initialize the client
    """

    def __init__(self, access_token: str = None):

        self._api = Api(access_token=access_token)

        self._categories = None
        self._customers = None
        self._discounts = None
        self._employees = None
        self._inventory = None
        self._items = None
        self._merchants = None
        self._modifiers = None
        self._payments = None
        self._pos_devices = None
        self._receipts = None
        self._shifts = None
        self._stores = None
        self._suppliers = None
        self._taxes = None
        self._variants = None

    def request(self, method: str, path: str, params: dict = None):
        """
        Client general request
        """

        return self._api.request(method, path, params=params)

    @property
    def customers(self):
        """
        Customers endpoint

        Returns:
            customers (loyverse.endpoints.Customer): Customer endpoint wrapper
        """

        if self._customers is None:
            from loyverse.endpoints import Customers
            self._customers = Customers(self._api)
        return self._customers

    @property
    def receipts(self):
        """
        Receipts endpoint

        Returns:
            receipts (loyverse.endpoints.Receipts): Receipts endpoint wrapper
        """

        if self._receipts is None:
            from loyverse.endpoints import Receipts
            self._receipts = Receipts(self._api)

        return self._receipts
