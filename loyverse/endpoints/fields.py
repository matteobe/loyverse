"""
Relevant fields to extract from API responses
"""

from collections import defaultdict


class AttributeDict(defaultdict):
    def __init__(self):
        super(AttributeDict, self).__init__(AttributeDict)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self[key] = value


receipt_fields = AttributeDict()
receipt_fields.receipt = ['receipt_number', 'note', 'receipt_type', 'refund_for', 'order', 'created_at', 'updated_at',
                          'source', 'receipt_date', 'cancelled_at', 'total_money', 'total_tax', 'points_earned',
                          'points_deducted', 'points_balance', 'customer_id', 'total_discount', 'employee_id',
                          'store_id', 'pos_device_id', 'dining_option', 'tip', 'surcharge']

receipt_fields.item = ['item_id', 'variant_id', 'item_name', 'variant_name', 'sku', 'quantity', 'price',
                       'gross_total_money', 'total_money', 'cost', 'cost_total', 'line_note', 'total_discount']

receipt_fields.payment = ['payment_type_id', 'name', 'type', 'money_amount', 'paid_at']

receipt_fields.payment_details = ['authorization_code', 'reference_id', 'entry_method', 'card_company', 'card_number']
