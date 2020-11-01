"""
Receipts endpoint wrapper class

Actions:
* get_by_query: get receipts that respect passed in query parameters
* get_by_id: get receipt passing valid ID
* get_by_date: get receipts for a given date
* get_by_dates: get receipts between two dates (if end-date is left empty, then it returns receipts until present day)
"""

import pandas as pd
from datetime import datetime
from loyverse.api import Api


class Receipts:

    def __init__(self, api: Api):
        self._api = api
        self._path = 'receipts'

    def get_by_query(self, **kwargs):
        """
        Retrieves receipts that respect the specific query criteria passed in

        Args:
            **kwargs:  all possible value-pairs that can be used to query the list
            # TODO: List here the query parameters
        Returns:
            response (dict): un-formatted receipts information (JSON)
        """

        return self._api.request('GET', self._path, params=kwargs)

    def get_by_id(self, receipt_id: str):
        """
        Retrieves the receipts information for a specific receipt ID
        Args:
            receipt_id (str): string uniquely identifying the receipt to be retrieved
        Returns:
            response (dict): un-formatted receipt information (JSON)
        """

        return self._api.request('GET', f'{self._path}/{receipt_id}')

    def get_by_date(self, date: datetime):
        """
        Retrieve receipts information for a specific day
        Args:
            date (datetime): datetime object representing day in question (including time zone info)
        Returns:
            response (dict): un-formatted receipts information (JSON)
        """

        timestamp_start = f"{date.strftime('%Y-%m-%d')}T00:00:00.000Z"
        timestamp_end = f"{date.strftime('%Y-%m-%d')}T23:59:59.999Z"
        data = self.get_by_query(created_at_min=timestamp_start,
                                 created_at_max=timestamp_end
                                 )
        return data

    def get_by_dates(self, start_date: datetime, end_date: datetime = datetime.now()):
        """
        Retrieves receipts information for a specific date interval.
        Args:
            start_date (datetime): start date, including time-zone info
            end_date (datetime): end date, including time-zone info (if not provided, defaults to datetime.now())
        Returns:
            response (dict): un-formatted receipts information (JSON)
        """

        timestamp = f"{start_date.strftime('%Y-%m-%d')}T00:00:00.000Z"

        return self.get_by_query(created_at_min=timestamp)



    @staticmethod
    def _receipt_formatter(data: dict):
        """
        Formats the passed-in receipt data into two dataframes containing receipts and items information.
        """
        # TODO: Implement categories to extract from the receipt dictionary
        # TODO: Return receipt info, items info with link to receipt ID and payment info w/ link to receipt ID

        receipt_id = data['receipt_number']

        receipt = pd.DataFrame({
            'id': receipt_id,
            'date': data['receipt_date'],
            'amount': data['total_money']
        }, index=[0])

        items = []
        for line_item in data['line_items']:
            item = pd.DataFrame({
                'name': line_item['item_name'],
                'price': line_item['price'],
                'quantity': line_item['quantity'],
                'receipt_id': receipt_id,
            }, index=[0])

            items.append(item)

        items = pd.concat(items)

        return receipt, items

    @staticmethod
    def _receipts_list_formatter(data: dict):
        """
        Formats the passed-in receipt data into two dataframes containing receipts and items information.
        """

        receipts = []
        items = []

        for receipt in data['receipts']:
            receipt_df, item_df = Receipts._receipt_formatter(receipt)
            receipts.append(receipt_df)
            items.append(item_df)

        receipts = pd.concat(receipts)
        items = pd.concat(items)

        return receipts, items
