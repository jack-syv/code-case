Certain assumptions were made, I assumed the property_id is unique, and identified by "bruksnummer, bnr or gårdsnummer"
The property_id should ideally be validated against a central registry, ensuring that the bnr exists at the supplied address or some similar solution.

In addition, some handling of lower case / uppercase strings may be necessary for unit_type and features. In addition to validation of the address, (e.g. it exists in the country)


Install neccessary dependencies by running
```
pip install -r requirements.txt
```

Run with 
```
python main.py
```

Swagger will be available at http://127.0.0.1:5000

Run unittests with 
```
python -m unittest tests/apis/test_property.py
```
