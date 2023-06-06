import unittest
from flask import Flask
from flask_restx import Api
from flask_restx._http import HTTPStatus
from apis.property import api

class PropertyApiTests(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(api)
        self.client = self.app.test_client()

    def test_create_property_invalid_floors(self):
        property_id = '49834'
        property_data = {
            'address': 'Oslo Gate 8',
            'number_of_floors': -2,
            'unit_type': 'house',
            'features': ['balcony']
        }

        response = self.client.post(f'/property/{property_id}', json=property_data)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(response.json, {'message': 'Number of floors must be 0 or above.'})

    def test_create_property(self):
        property_id = '49834'
        property_data = {
            'address': 'Oslo Gate 8',
            'number_of_floors': 2,
            'unit_type': 'house',
            'features': ['balcony']
        }

        response = self.client.post(f'/property/{property_id}', json=property_data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json, 'Property with property id: ' + property_id + ' succesfully created.')

    def test_create_existing_property(self):
        property_id = '12345'
        property_data = {
            'address': 'Oslo Gate 9',
            'number_of_floors': 1,
            'unit_type': 'apartment',
            'features': ['fireplace', 'balcony']
        }

        self.client.post(f'/property/{property_id}', json=property_data)

        # Try to create the same property again
        response = self.client.post(f'/property/{property_id}', json=property_data)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(response.json, {'message': 'Property already exists'})

    def test_update_property_invalid_unit_type(self):
        property_id = '49834'
        property_data = {
            'address': 'Oslo Gate 8',
            'number_of_floors': 2,
            'unit_type': 'swimming pool',
            'features': ['balcony']
        }

        response = self.client.put(f'/property/{property_id}', json=property_data)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(response.json, {'message': 'Invalid unit_type. Allowed values: house, apartment, serialhouse'})

if __name__ == '__main__':
    unittest.main()