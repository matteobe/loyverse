"""
Customers endpoint wrapper class

Possible requests:

* get_by_query: get customers that respect passed in query parameters
* get_by_id: get customer with given customer ID
* get_by_email: get customer with given email
* get_by_creation_date: get customers created at specific date
* get_by_creation_dates: get customers created between specific dates
"""

from datetime import datetime, timezone
from loyverse.api import Api
from loyverse.utils.dates import utc_isoformat, day_start, day_end


class Customers:

    def __init__(self, api: Api):
        self._api = api
        self._path = 'customers'

    def get_by_query(self, customer_ids: list = None, email: str = None,
                     created_at_min: datetime = None, created_at_max: datetime = None,
                     updated_at_min: datetime = None, updated_at_max: datetime = None,
                     limit: int = 250, cursor: str = None) -> dict:
        """
        Retrieves customers that respect the specific query criteria passed in. A detailed description of the query
        parameters is available `here <https://developer.loyverse.com/docs/#tag/Customers/paths/~1customers/get>`_.

        Args:
            customer_ids (list): filter customers by customer id
            email (str): filter customer by email
            created_at_min (datetime): filter customers created after this date (includes timezone info)
            created_at_max (datetime): filter customers created before this date (includes timezone info)
            updated_at_min (datetime): filter customers updated after this date (includes timezone info)
            updated_at_max (datetime): filter customers updated before this date (includes timezone info)
            limit (int): maximum number of customers to return per request (1 to 250)
            cursor (str): token to get continuation of return list for requests exceeding limits
        Returns:
            response (dict): formatted customers information (JSON)
        """

        params = dict()

        if customer_ids is not None:
            params['customer_ids'] = ','.join(customer_ids)

        if email is not None:
            params['email'] = email

        if created_at_min is not None:
            params['created_at_min'] = utc_isoformat(created_at_min)

        if created_at_max is not None:
            params['created_at_max'] = utc_isoformat(created_at_max)

        if updated_at_min is not None:
            params['updated_at_min'] = utc_isoformat(updated_at_min)

        if updated_at_max is not None:
            params['updated_at_max'] = utc_isoformat(updated_at_max)

        if limit is not None:
            params['limit'] = limit

        if cursor is not None:
            params['cursor'] = cursor

        return self._api.request('GET', self._path, params=params)

    def get_by_id(self, customer_id: str) -> dict:
        """
        Retrieves the customer information for specific customer ID

        Args:
            customer_id (str): string uniquely identifying the customer to be retrieved
        Returns:
            response (dict): formatted customer information (JSON)
        """

        return self._api.request('GET', f'{self._path}/{customer_id}')

    def get_by_email(self, email: str) -> dict:
        """
        Retrieves the customer information for a user with the specific email

        Args:
            email (str): email identifying the customer to be retrieved
        Returns:
            response (dict): formatted customer information (JSON)
        """

        return self.get_by_query(email=email)

    def get_by_creation_date(self, date: datetime) -> dict:
        """
        Retrieve customers information for a specific creation date

        Args:
            date (datetime): datetime object representing day in question (including time zone info)
        Returns:
            response (dict): formatted customers information (JSON)
        """

        data = self.get_by_query(created_at_min=day_start(date),
                                 created_at_max=day_end(date),
                                 )
        return data

    def get_by_creation_dates(self, start_date: datetime, end_date: datetime = None) -> dict:
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

        data = self.get_by_query(created_at_min=day_start(start_date),
                                 created_at_max=day_end(end_date),
                                 )
        return data

    # TODO: Implement parsing to dataframes
