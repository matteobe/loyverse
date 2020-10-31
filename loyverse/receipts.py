"""
Loyverse Receipts API wrapper
"""

from datetime import datetime
import pandas as pd
from .clients import LoyverseAPI


class ReceiptsAPI(LoyverseAPI):
    """
    Receipts specific wrapper class
    """

    def __init__(self):
        super().__init__()
        self.path = 'receipts'

    def get_by_id(self, receipt_id: str):
        """
        Retrieves API data for a specific receipt ID
        Args:
            receipt_id (str): string uniquely identifying the receipt to be retrieved
        Returns:
            data (dict): un-formatted receipt information
        """

        data = self.get(f'{self.path}/{receipt_id}')

        return data

    def get_list(self, **kwargs):
        """
        Retrieves API data for a list of receipts

        Args:
            **kwargs:  all possible value-pairs that can be used to query the list
        """

        data = self.get(f'{self.path}', params=kwargs)

        return data

    def get_from_date(self, date: datetime):
        """
        Retrieves list of receipts starting at a specific date
        """

        timestamp = f"{date.strftime('%Y-%m-%d')}T00:00:00.000Z"
        data = self.get_list(created_at_min=timestamp)

        return data

    def get_by_date(self, date: datetime):
        """
        Retrieves list of receipts for a specific date
        """

        timestamp_start = f"{date.strftime('%Y-%m-%d')}T00:00:00.000Z"
        timestamp_end = f"{date.strftime('%Y-%m-%d')}T23:59:59.999Z"
        data = self.get_list(created_at_min=timestamp_start,
                             created_at_max=timestamp_end
                             )
        return data

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
            receipt_df, item_df = ReceiptsAPI._receipt_formatter(receipt)
            receipts.append(receipt_df)
            items.append(item_df)

        receipts = pd.concat(receipts)
        items = pd.concat(items)

        return receipts, items
