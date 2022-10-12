# Initializing the project

- [x] Execute `fixture_parser.py` if data is not already in json format
  
  ```python fixture_parser.py investors```

  ```python fixture_parser.py investments```

- [ ] Create DB

  ```python manage.py migrate```

- [ ] Populate DB with fixtures

  ```python manage.py loaddata investors investments```

## Launch server

```python manage.py runserver 8000```

Explore endpoints in localhost:8000/api

# Basic e2e

To perform a basic e2e test of the requested funcionalities (create all bills, create a couple cashcalls, edit status of a cashcall):

```python client.py e2e```

## Create Bills

To create all Bills based on Investments data, you must execute a POST request to /api/bills/create-all/

This script is already prepared in the file client.py as

```python client.py create-bills```

## Retrieve Bills of investor

To retrieve Bills filtered by investor, you must execute GET request to /api/bills/investor/<investor_id>

## Create Cashcall

To create Cashcall for specific investor, you must execute a POST request to /api/cashcalls/create/<investor_id>

This script is already prepared in the file client.py as

```python client.py create-cashcall -investor_id <investor_id>```

## Update Cashcall

To update the status of a Cashcall, you must execute a PUT request to /api/cashcalls/<investor_id>/status with the payload {"invoice_status":"new_status"}

This script is already prepared in the file client.py as

```python client.py update-cashcall -cashcall_id <cashcall_id> -status <status>```

# Some changes made to DB

- Some data was edited to encompass edge cases. In particular, 6 entries of the investments.csv file changed to year 2022 (current year).
- Column 'IBAN' in cashcall.csv changed to 'credit', to respect investor type of payment in investors.csv 
- Other minor typos to column names
