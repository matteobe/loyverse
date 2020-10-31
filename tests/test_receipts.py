"""
Testing of API wrapper functionality.
"""

from datetime import datetime
from loyverse import ReceiptsAPI
from tests import store_json_response


def test_receipt_get_by_id():
    """
    Test ReceiptsAPI get_by_id call
    """

    receipt_id = '1-4076'
    api = ReceiptsAPI()

    receipt = api.get_by_id(receipt_id)

    store_json_response(receipt, 'receipt')
    assert isinstance(receipt, dict), "ReceiptAPI get_by_id return type not of type: dict."
    assert receipt['receipt_number'] == receipt_id, "The payment ID should be in the response."


def test_receipts_by_date():
    """
    Test ReceiptsAPI get_by_date call
    """

    api = ReceiptsAPI()
    date = datetime(2020, 10, 12)

    receipts = api.get_by_date(date)

    store_json_response(receipts, 'receipts')
