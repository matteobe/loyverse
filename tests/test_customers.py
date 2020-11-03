"""
Testing of Client.customers endpoint functions

Tests:
* test_get_by_id: testing get_by_id function
* test_get_by_date: testing get_by_date function
"""

import pytest
from datetime import datetime
from loyverse import Client
from loyverse.utils.dates import add_timezone
from tests.utils import error_msg


endpoint = 'customers'
timezone = 'Europe/Zurich'


@pytest.mark.vcr()
def test_get_customers_by_creation_dates():
    """
    Test Client.customers get_by_dates endpoint function
    """

    # Query arguments
    start_date = add_timezone(datetime(2019, 9, 1), timezone)
    end_date = add_timezone(datetime(2020, 10, 1), timezone)

    # Expected results
    customers_length = 0

    client = Client()
    customers = client.customers.get_by_creation_dates(start_date, end_date)

    assert isinstance(customers, dict), error_msg(endpoint, 'get_by_date return type not of type dict')
    assert len(customers[endpoint]) == customers_length, error_msg(endpoint, 'get_by_dates: incorrect number of '
                                                                             'customers retrieved')
