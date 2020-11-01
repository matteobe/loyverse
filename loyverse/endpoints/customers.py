"""
Customers endpoint wrapper class

Actions:
* get_by_query: get customers that respect passed in query parameters
* get_by_id: get customer by passing valid ID
"""

from loyverse.api import Api


class Customers:

    def __init__(self, api: Api):
        self._api = api
        self._path = 'customers'

    def get_by_query(self, **kwargs):
        """
        Retrieves customers that respect the specific query criteria passed in

        Args:
            **kwargs:  all possible value-pairs that can be used to query the list
            # TODO: List here the query parameters
        Returns:
            response (dict): un-formatted customers information (JSON)
        """

        return self._api.request('GET', self._path, params=kwargs)

    def get_by_id(self, customer_id: str):
        """
        Retrieves the receipts information for a specific receipt ID
        Args:
            customer_id (str): string uniquely identifying the receipt to be retrieved
        Returns:
            response (dict): un-formatted receipt information (JSON)
        """

        return self._api.request('GET', f'{self._path}/{customer_id}')
