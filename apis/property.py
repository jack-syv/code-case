from flask import request, abort, make_response
from flask_restx import Resource, Namespace, fields
from apis.validation.property_validation import validate_property
from repository import property_repository
from .utils.types import valid_unit_types, valid_features

api = Namespace('property', description='Endpoints for handling a property')

# Model for the property
property_model = api.model('Property', {
    'address': fields.String(required=True, description='Address of the property'),
    'number_of_floors': fields.Integer(required=True, description='Number of floors'),
    'unit_type': fields.String(required=True, description='The type of property, must be one of ' + str(valid_unit_types)),
    'features':fields.List(fields.String, required=True, description='Main features of the property, must be one or more of ' + str(valid_features))
})

@api.route('/<property_id>', endpoint="Property with id")
@api.doc(params={'property_id': 'The specific id of the property that is requested'})
class Property(Resource):

    """Endpoints for creating, updating and deleting a property with a specific property id."""
    
    @api.doc(responses={200: "Ok", 400: "Bad Request", 500: "Internal error"}, description="Create a Property")
    @api.expect(property_model)
    def post(self, property_id):
        property_data = request.json
        validate_property(property_data)
        if property_repository.get_property(property_id) is not None:
            error_msg = "Property already exists"
            return make_response({'message': error_msg}, 400)
        
        if property_repository.create_property(property_id, property_data):
            return "Property with property id: " + property_id + " succesfully created."
        return abort(400)
    
    @api.doc(responses={200: "Ok", 400: "Bad Request", 500: "Internal error"}, description="Update a Property")
    @api.expect(property_model)
    def put(self, property_id): 
        property_data = request.json
        validate_property(property_data)
        if property_repository.update_property(property_id, property_data):
            return "Property with property_id " + property_id + " successfully updated."
        else:
            return property_bad_request(property_id)
    
    @api.doc(responses={200: "Ok", 400: "Bad Request", 500: "Internal error"}, description="Delete a Property")
    def delete(self, property_id):
        if property_repository.delete_property(property_id):
            return "Property with property_id " + property_id + " succesfully deleted."
        else:
            return property_bad_request(property_id)

    
def property_bad_request(property_id):
    error_msg = "Property with property_id " + property_id + " does not exist."
    return make_response({'message': error_msg}, 400)