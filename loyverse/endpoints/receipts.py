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
from loyverse.endpoints.fields import receipt_fields


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

        receipt_id = receipt['receipt_number']

        receipt_df = pd.DataFrame({key: receipt[key] for key in receipt_fields.receipt}, index=[0])

        items_df = []
        for line_item in receipt['line_items']:
            item = {key: line_item[key] for key in receipt_fields.item}
            item['receipt_number'] = receipt_id
            item = pd.DataFrame(item, index=[0])
            items_df.append(item)

        items_df = pd.concat(items_df)

        payments_df = []
        for payment_item in receipt['payments']:
            payment = {key: payment_item[key] for key in receipt_fields.payment}
            payment['receipt_number'] = receipt_id
            details = payment_item['payment_details']

            if details is None:
                payment_details = {key: None for key in receipt_fields.payment_details}
            else:
                payment_details = {key: details[key] for key in receipt_fields.payment_details}

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
