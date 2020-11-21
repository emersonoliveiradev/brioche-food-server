from flask import abort, jsonify
from flask_restful import Resource, fields, marshal_with
from briochefood.models import User


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
}

user_fields = {
    "id": fields.Integer,
    "name": fields.String(),
    "lastname": fields.String,    
    "email": fields.String,
    "cpf": fields.String,
    "phone": fields.String,
    "status": fields.String,       
    "createdAt": fields.DateTime(attribute='created_at', dt_format='iso8601'), 
    "updatedAt": fields.DateTime(attribute='updated_at', dt_format='iso8601'), 
    'address': fields.Nested(address_fields)
}

class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self):        
        users = User.query.all() or abort(204)        
        return users


class UserItemResource(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first() or abort(404)
        return jsonify(user.to_dict())