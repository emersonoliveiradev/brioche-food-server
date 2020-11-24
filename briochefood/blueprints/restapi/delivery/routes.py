from flask import abort, jsonify
from flask_restful import Resource
from briochefood.models import Delivery
from briochefood.ext.serialization import DeliverySchema


class DeliveryResource(Resource):
    def get(self):
        """Get all deliveries"""
        deliveries = Delivery.query.all()
        schema = DeliverySchema(many=True)
        return schema.jsonify(deliveries)


class DeliveryItemResource(Resource):
    def get(self, delivery_id):
        """Get delivery"""
        delivery = Delivery.query.filter_by(
            id=delivery_id).first() or abort(404, "Item not found")
        schema = DeliverySchema(many=False)
        return schema.jsonify(delivery)
