"""
Testing of API wrapper functionality.
"""

from datetime import datetime
from loyverse.client import Client
from tests import save_json


def test_receipt_get_by_id():
    """
    Test ReceiptsAPI get_by_id call
    """

    receipt_id = '1-4076'
    client = Client()

    receipt = client.receipts.get_by_id(receipt_id)

    save_json(receipt, 'receipt')
    assert isinstance(receipt, dict), "ReceiptAPI get_by_id return type not of type: dict."
    assert receipt['receipt_number'] == receipt_id, "The payment ID should be in the response."


def test_receipts_by_date():
    """
    Test ReceiptsAPI get_by_date call
    """

    date = datetime(2020, 10, 12)
    client = Client()

    receipts = client.receipts.get_by_date(date)

    save_json(receipts, 'receipts')
