"""
Loyverse Customers API wrapper
"""

from .clients import LoyverseAPI


class CustomersAPI(LoyverseAPI):
    """
    Customers specific wrapper class
    """

    def __init__(self):
        super().__init__()
        self.path = 'customers'

    def get_by_id(self, customer_id: str):
        """
        Retrieves API data for a specific customer ID
        Args:
            customer_id (str): string uniquely identifying the customer to be retrieved
        Returns:
            data (dict): un-formatted customer information
        """

        data = self.get(f'{self.path}/{customer_id}')

        return data
