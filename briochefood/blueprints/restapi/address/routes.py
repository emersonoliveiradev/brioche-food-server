from flask import abort, jsonify
from flask_restful import Resource, fields, marshal_with
from briochefood.models import Address


user_fields = {
    "id": fields.Integer,
    "name": fields.String(),
    "lastname": fields.String,    
    "email": fields.String,
    "cpf": fields.String,
    "phone": fields.String,
    "status": fields.String,       
    "createdAt": fields.DateTime(attribute='created_at', dt_format='iso8601'), 
    "updatedAt": fields.DateTime(attribute='updated_at', dt_format='iso8601') 
}

address_fields = {
    'id': fields.Integer,
    'street': fields.String,    
    'number': fields.Integer,
    'complement': fields.String,
    'district': fields.String,
    'city': fields.String,
    'cep': fields.String,
    'state': fields.String,
    'country': fields.String,    
    "createdAt": fields.DateTime(attribute='created_at', dt_format='iso8601'), 
    "updatedAt": fields.DateTime(attribute='updated_at', dt_format='iso8601'), 
    'user': fields.Nested(user_fields)
}

class AddressResource(Resource):    
    @marshal_with(address_fields)
    def get(self):                
        addresses = Address.query.all() or abort(204)      
        return addresses 
        

