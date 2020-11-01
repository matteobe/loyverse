"""
Loyverse API client

The Client class encapsulates the endpoints of the Loyverse API and provides a single point of initialization for
API requests.

The Client class exposes the following end-points
* receipts
    * list:  GET /receipts
    * id: GET /receipts/<id>
* customers
    * id: GET /customers/<id>
"""

from loyverse.api import Api


class Client:
    """Loyverse API client
    Args:
        access_token (str): Access token string to be used to initialize the client
    """

    def __init__(self, access_token: str = None):

        self._api = Api(access_token=access_token)

        self._receipts = None
        self._customers = None

    def request(self, method: str, path: str, params: dict = None):
        """
        Client general request
        Args:
            method (str):
            path (str):
            params (dict):
        Returns:
            response (dict):
        """

        return self._api.request(method, path, params=params)

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
