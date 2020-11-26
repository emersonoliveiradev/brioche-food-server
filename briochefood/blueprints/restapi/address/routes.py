from flask import abort
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from briochefood.models import Address
from briochefood.ext.serialization import AddressSchema


class AddressResource(Resource):
    @jwt_required
    def get(self):
        schema = AddressSchema(many=True)
        addresses = Address.query.all() or abort(204, "No items found")
        return schema.jsonify(addresses)


class AddressItemResource(Resource):
    @jwt_required
    def get(self, address_id):
        schema = AddressSchema(many=False)
        addresses = Address.query.filter_by(
            id=address_id).first() or abort(404, "Item not found")
        return schema.jsonify(addresses)
