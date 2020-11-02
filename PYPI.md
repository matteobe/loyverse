The loyverse package provides a wrapper around the [Loyverse API](https://developer.loyverse.com/docs/).
It is intended to help Loyverse users to access their data using Python, without the need for 
boilerplate code. Furthermore, the package provides tools to convert the API responses into 
[pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) DataFrames for easier manipulation. 

### Getting started
The package relies on a central Client object to access all available endpoints. 
To start a new client, the user either needs to provide the access token explicitly, or 
store it in the environmental variables under LOYVERSE_ACCESS_TOKEN. For how to generate your access token, please
 check 
 [here](https://help.loyverse.com/help/loyverse-api#:~:text=To%20create%20a%20new%20token,Access%20token%20will%20be%20created.).

The example below shows how to initialize a client:

```python
from loyverse import Client

# Pass API access token explicitly
client = Client(access_token='your_access_token')

# Pass API access token using environment variable LOYVERSE_ACCESS_TOKEN
client = Client()
```

### Access an endpoint

All exposed API endpoints are available as properties of the Client class. Currently, the following 
endpoints are implemented:

* Customers
* Receipts

The example below shows how to retrieve receipts information for a specific date:

```python
from datetime import datetime
from loyverse import Client

target_date = datetime(2020, 10, 31)

# Retrieve receipts data
client = Client()
response = client.receipts.get_by_date(target_date)

# Convert to dataframes
receipts, items, payments = client.receipts.to_dataframes(response)
```
