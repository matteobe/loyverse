# Loyverse API wrapper

[![Loyverse API version](https://img.shields.io/badge/API-v1.0-yellow.svg)](https://shields.io/)
[![PyPi Latest Release](https://img.shields.io/pypi/v/loyverse)](https://pypi.org/project/loyverse/)
[![PyPi - Status](https://img.shields.io/pypi/status/loyverse)](https://pypi.org/project/loyverse/)
[![GitHub Release Date](https://img.shields.io/github/release-date/matteobe/loyverse)](https://img.shields.io/github/release-date/matteobe/loyverse)
[![PyPi Downloads](https://img.shields.io/pypi/dm/loyverse)](https://pypistats.org/packages/loyverse)
[![Documentation Status](https://readthedocs.org/projects/loyverse/badge/?version=latest)](https://loyverse.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/github/license/matteobe/loyverse)](https://github.com/matteobe/loyverse/blob/master/LICENSE)
[![Made with python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Made with sphinx](https://img.shields.io/badge/Made%20with-Sphinx-1f425f.svg)](https://www.sphinx-doc.org/)

The loyverse package provides a wrapper around the [Loyverse API v1.0](https://developer.loyverse.com/docs/).
It is intended to help Loyverse users to access their data using Python, without the need for boilerplate code. 
Furthermore, the package provides tools to convert the API responses into 
[pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) DataFrames for easier manipulation. 


## Getting started
The package relies on a central Client object to access all available endpoints. 
To start a new client, the user either needs to provide the access token explicitly, or store it in the environmental 
variables under LOYVERSE_ACCESS_TOKEN. For how to generate your access token, please check 
[here](https://help.loyverse.com/help/loyverse-api#:~:text=To%20create%20a%20new%20token,Access%20token%20will%20be%20created.).

The example below shows how to initialize a client object:

```python
from loyverse import Client

# Pass API access token explicitly
client = Client(access_token='your_access_token')

# Pass API access token using an environment variable LOYVERSE_ACCESS_TOKEN
client = Client()
```


## Access endpoints

All exposed API endpoints are available as properties of the Client class (i.e. client.endpoint). Currently, the
following endpoints are implemented:

* Customers
* Receipts

The example below shows how to retrieve receipts information for a specific date:

```python
from datetime import datetime
from loyverse import Client
from loyverse.utils.dates import add_timezone

# Initialize client
client = Client(access_token='your_access_token')

# Retrieve receipt data for a specific receipt
receipt_id = 'XXXX'
response = client.receipts.get_by_id(receipt_id)

# Retrieve receipts data for a specific date (timezone-aware)
target_date = add_timezone(datetime(2020, 10, 31), 'Europe/Zurich')
response = client.receipts.get_by_date(target_date)

# Retrieve receipts data for a specific date range (timezone-aware)
# Start date: 2020-Oct-31 12:00 Central European Time
# End date: 2020-Nov-4 12:00 Central European Time
start_date = add_timezone(datetime(2020, 10, 31, 12, 0), 'Europe/Zurich')
end_date = add_timezone(datetime(2020, 11, 4, 12, 0), 'Europe/Zurich')

# Convert to dataframes
receipts, items, payments = client.receipts.to_dataframes(response)
```


## Contribute
Everyone is welcomed to contribute to this project. Please read the contribution guidelines 
[here](https://github.com/matteobe/loyverse/blob/master/CONTRIBUTING.md) for more details.
