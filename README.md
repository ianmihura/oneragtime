# Initializing the project

- [x] Execute `fixture_parser.py` if data is not already in json format
  
  ```python fixture_parser.py investors```

  ```python fixture_parser.py investments```

- [ ] Create DB

  ```python manage.py migrate```

- [ ] Populate DB with fixtures

  ```python manage.py loaddata investors investments```

# Launch server

```python manage.py runserver 8000```

Explore endpoints in localhost:8000

# Create Bills

To create all Bills based on Investments data, you must execute a POST request to /api/bills/create-all/

This script is already prepared in the file client.py as

```python client.py create-all```

# TODO

- [ ] URLs for all object responses (hyperlinks)
- [ ] create-all Bills
- [ ] Comment code
- [ ] investment fee_type -> data type
- [ ] bill fee_type -> data type
- [ ] cashcall status -> data type
- [ ] explorable endpoints (/api/)
- [ ] style create bills

# Other comments

Some data was edited to encompass edge cases. In particular, 6 entries of the investments.csv file changed to year 2022 (current year).