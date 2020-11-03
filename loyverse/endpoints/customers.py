"""
Customers endpoint wrapper class

Actions:

* get_by_query: get customers that respect passed in query parameters
* get_by_id: get customer by passing valid ID
"""

from datetime import datetime, timezone
from loyverse.api import Api
from loyverse.utils.dates import utc_isoformat, day_start, day_end


class Customers:

    def __init__(self, api: Api):
        self._api = api
        self._path = 'customers'

    def get_by_query(self, **kwargs):
        """
        Retrieves customers that respect the specific query criteria passed in

        Args:
            **kwargs:  all possible value-pairs that can be used to query the list.
                A detailed description of the query parameters is available
                `here <https://developer.loyverse.com/docs/#tag/Customers/paths/~1customers/get>`_.
        Returns:
            response (dict): formatted customers information (JSON)
        """

        return self._api.request('GET', self._path, params=kwargs)

    def get_by_id(self, customer_id: str):
        """
        Retrieves the customer information for a specific customer ID

        Args:
            customer_id (str): string uniquely identifying the customer to be retrieved
        Returns:
            response (dict): formatted customer information (JSON)
        """

        return self._api.request('GET', f'{self._path}/{customer_id}')

    def get_by_email(self, email: str):
        """
        Retrieves the customer information for a user with the specific email

        Args:
            email (str): email identifying the customer to be retrieved
        Returns:
            response (dict): formatted customer information (JSON)
        """

        return self.get_by_query(email=email)

    def get_by_creation_date(self, date: datetime):
        """
        Retrieve customers information for a specific creation date

        Args:
            date (datetime): datetime object representing day in question (including time zone info)
        Returns:
            response (dict): formatted customers information (JSON)
        """

        timestamp_start = utc_isoformat(day_start(date))
        timestamp_end = utc_isoformat(day_end(date))
        data = self.get_by_query(created_at_min=timestamp_start,
                                 created_at_max=timestamp_end,
                                 )
        return data

    def get_by_creation_dates(self, start_date: datetime, end_date: datetime = None):
        """
        Retrieve customers information for a creation date range

        Args:
            start_date (datetime): datetime object representing starting day in question (including time zone info)
            end_date (datetime): datetime object for end-date (default: UTC now)
        Returns:
            response (dict): formatted customers information (JSON)
        """

        if end_date is None:
            end_date = datetime.now(timezone.utc)

        timestamp_start = utc_isoformat(start_date)
        timestamp_end = utc_isoformat(end_date)
        data = self.get_by_query(created_at_min=timestamp_start,
                                 created_at_max=timestamp_end,
                                 )
        return data
