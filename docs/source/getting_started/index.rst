.. _getting_started:

Getting started
=====================

Authorization
--------------

Access to the Loyverse API is granted through an access token, please check
`here <https://help.loyverse.com/help/loyverse-api#:~:text=To%20create%20a%20new%20token,Access%20token%20will%20be%20created.>`_
for a detailed description on how to create one.


Initialize a client
-------------------

The Loyverse API is accessed using a single client, which can in turn be used to access all implemented endpoints.

.. code-block:: python

    from loyverse import Client

    # Initialize by passing access token
    client = Client(access_token='your_token_here')

    # Initialize using environment variables (access_token stored in environment variable: LOYVERSE_ACCESS_TOKEN)
    client = Client()

Access endpoints
----------------

Once the client is initialized, we can access endpoints by accessing attributes of the client object.
Currently, the following endpoints are available:

* Customers
* Receipts

For a detailed description of all available endpoints and response data structure, please refer to the
`Loyverse API documentation <https://developer.loyverse.com/docs/>`_.

Below you can find an example of how to access the receipts endpoint and retrieve receipt information for a specific
receipt, a specific date or a date range (as datetime objects).

.. code-block:: python

   # JSON format response
   response = client.receipts.get_by_id('receipt_id')
   response = client.receipts.get_by_date(date)
   response = client.receipts.get_by_dates(start_date, end_date)

   # Format to pandas dataframes
   receipts, items, payments = client.receipts.to_dataframes(response)
