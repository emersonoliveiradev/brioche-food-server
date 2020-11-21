from flask import abort, jsonify
from flask_restful import Resource
from briochefood.models import Delivery


class DeliveryResource(Resource):
    def get(self):
        deliveries = Delivery.query.all() or abort(204)
        return jsonify(
            {"deliveries": [delivery.to_dict() for delivery in deliveries]}
        )


class DeliveryItemResource(Resource):
    def get(self, delivery_id):
        delivery = Delivery.query.filter_by(
            id=delivery_id).first() or abort(404)
        return jsonify(delivery.to_dict())
