"""
Receipts endpoint wrapper class

Possible requests:

* get_by_query: get receipts that respect passed in query parameters
* get_by_id: get receipt with a given ID
* get_by_date: get receipts for a given date
* get_by_dates: get receipts between two dates
"""

import pandas as pd
from datetime import datetime, timezone
from loyverse.api import Api
from loyverse.utils.dates import utc_isoformat, day_start, day_end
from loyverse.endpoints.fields import receipt as fields


class Receipts:

    def __init__(self, api: Api):
        self._api = api
        self._path = 'receipts'

    def get_by_query(self, receipt_numbers: list = None, since_receipt_number: str = None,
                     before_receipt_number: str = None, store_id: str = None, order: str = None, source: str = None,
                     updated_at_min: datetime = None, updated_at_max: datetime = None,
                     created_at_min: datetime = None, created_at_max: datetime = None, limit: int = 250,
                     cursor: str = None) -> dict:
        """
        Retrieves receipts that respect the specific query criteria passed in. A detailed description of the query 
        parameters is available `here <https://developer.loyverse.com/docs/#tag/Receipts/paths/~1receipts/get>`_.

        Args:
            receipt_numbers (list): filter receipts by receipt numbers
            since_receipt_number (str): return only receipts after this receipt number
            before_receipt_number (str): return only receipts before this receipt number
            store_id (str): filter receipts by store id
            order (str): filter receipts by order
            source (str): filter receipts by source (e.g. My app)
            updated_at_min (datetime): filter receipts updated after this date (includes timezone info)
            updated_at_max (datetime): filter receipts updated before this date (includes timezone info)
            created_at_min (datetime): filter receipts created after this date (includes timezone info)
            created_at_max (datetime): filter receipts created before this date (includes timezone info)
            limit (int): maximum number of receipts to return per request (1 to 250)
            cursor (str): token to get continuation of return list for requests exceeding limits
        Returns:
            response (dict): formatted receipts information (JSON)
        """

        params = dict()

        if receipt_numbers is not None:
            params['receipt_numbers'] = ','.join(receipt_numbers)

        if since_receipt_number is not None:
            params['since_receipt_number'] = since_receipt_number

        if before_receipt_number is not None:
            params['before_receipt_number'] = before_receipt_number

        if store_id is not None:
            params['store_id'] = store_id

        if order is not None:
            params['order'] = order

        if source is not None:
            params['source'] = source

        if updated_at_min is not None:
            params['updated_at_min'] = utc_isoformat(updated_at_min)

        if updated_at_max is not None:
            params['updated_at_max'] = utc_isoformat(updated_at_max)

        if created_at_min is not None:
            params['created_at_min'] = utc_isoformat(created_at_min)

        if created_at_max is not None:
            params['created_at_max'] = utc_isoformat(created_at_max)

        if limit is not None:
            params['limit'] = limit

        if cursor is not None:
            params['cursor'] = cursor

        response = self._api.request('GET', self._path, params=params)

        return response

    def get_by_id(self, receipt_id: str) -> dict:
        """
        Retrieves the receipts information for a specific receipt ID

        Args:
            receipt_id (str): string uniquely identifying the receipt to be retrieved
        Returns:
            response (dict): formatted receipt information (JSON)
        """

        return self._api.request('GET', f'{self._path}/{receipt_id}')

    def get_by_date(self, date: datetime) -> dict:
        """
        Retrieve receipts information for a specific day

        Args:
            date (datetime): datetime object representing day in question (including time zone info)
        Returns:
            response (dict): formatted receipts information (JSON)
        """

        data = self.get_by_query(created_at_min=day_start(date),
                                 created_at_max=day_end(date),
                                 )
        return data

    def get_by_dates(self, start_date: datetime, end_date: datetime = None) -> dict:
        """
        Retrieves receipts information for a specific date interval.

        Args:
            start_date (datetime): start date, including time-zone info
            end_date (datetime): end date, including time-zone info (if not provided, defaults to UTC now)
        Returns:
            response (dict): formatted receipts information (JSON)
        """

        if end_date is None:
            end_date = datetime.now(timezone.utc)

        data = self.get_by_query(created_at_min=day_start(start_date),
                                 created_at_max=day_end(end_date),
                                 )
        return data

    @staticmethod
    def _receipt_to_dataframes(receipt: dict):
        """
        Formats one receipts object into three dataframes, containing receipts and items information.

        Args:
            receipt (dict): a receipt object
        Returns:
            receipt_df (pandas.Dataframe): receipt level information
            items_df (pandas.Dataframe): receipt items information
            payments_df (pandas.Dataframe): receipt payments information
        """

        if 'receipts' in receipt:
            raise ValueError('Invalid receipt object passed in, should not contain - receipts - field')

        id_key = 'receipt_number'

        receipt_df = pd.DataFrame({key: receipt[key] for key in fields.receipt}, index=[0])

        items_df = []
        for line_item in receipt['line_items']:
            item = {key: line_item[key] for key in fields.item}
            item[id_key] = receipt[id_key]
            item = pd.DataFrame(item, index=[0])
            items_df.append(item)

        items_df = pd.concat(items_df)

        payments_df = []
        for payment_item in receipt['payments']:
            payment = {key: payment_item[key] for key in fields.payment}
            payment[id_key] = receipt[id_key]
            details = payment_item['payment_details']

            if details is None:
                payment_details = {key: None for key in fields.payment_details}
            else:
                payment_details = {key: details[key] for key in fields.payment_details}

            payment = {**payment, **payment_details}
            payment = pd.DataFrame(payment, index=[0])
            payments_df.append(payment)

        payments_df = pd.concat(payments_df)

        return receipt_df, items_df, payments_df

    @staticmethod
    def to_dataframes(response: dict):
        """
        Formats receipts API return data into three dataframes (receipts, items, payments)

        Args:
            response (dict): receipt endpoint response
        Returns:
            receipt_df (pandas.Dataframe): receipt level information
            items_df (pandas.Dataframe): receipt items information
            payments_df (pandas.Dataframe): receipt payments information
        """

        receipts = []
        items = []
        payments = []

        if 'receipts' in response:
            receipts_in = response['receipts']
        else:
            receipts_in = [response]

        for receipt in receipts_in:
            receipt_df, item_df, payment_df = Receipts._receipt_to_dataframes(receipt)
            receipts.append(receipt_df)
            items.append(item_df)
            payments.append(payment_df)

        receipts = pd.concat(receipts)
        items = pd.concat(items)
        payments = pd.concat(payments)

        receipts.reset_index(drop=True, inplace=True)
        items.reset_index(drop=True, inplace=True)
        payments.reset_index(drop=True, inplace=True)

        return receipts, items, payments
