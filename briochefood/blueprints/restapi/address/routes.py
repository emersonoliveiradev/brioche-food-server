from flask import abort
from flask_restful import Resource
from briochefood.models import Address
from briochefood.ext.serialization import AddressSchema


class AddressResource(Resource):
    def get(self):
        schema = AddressSchema(many=True)
        addresses = Address.query.all() or abort(204)
        return schema.jsonify(addresses)


class AddressItemResource(Resource):
    def get(self, address_id):
        schema = AddressSchema(many=False)
        addresses = Address.query.filter_by(
            id=address_id).first() or abort(404)
        return schema.jsonify(addresses)
