from flask import abort
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required
from briochefood.ext.database import db
from briochefood.models import Delivery
from briochefood.ext.serialization import DeliverySchema, UpdateDeliverySchema


class DeliveryResource(Resource):
    @jwt_required
    def get(self):
        """Get all deliveries"""
        deliveries = Delivery.query.all()
        schema = DeliverySchema(many=True)
        return schema.jsonify(deliveries)

    @jwt_required
    def post(self):
        """Update delivery status"""
        schema = UpdateDeliverySchema()
        data = schema.load(request.get_json(force=True))

        delivery = Delivery.query.filter_by(
            id=data['id']).first() or abort(404, "Item not found")
        delivery.status = data['status']

        db.session.add(delivery)
        db.session.commit()

        return schema.jsonify(delivery)


class DeliveryItemResource(Resource):
    @jwt_required
    def get(self, delivery_id):
        """Get delivery"""
        delivery = Delivery.query.filter_by(
            id=delivery_id).first() or abort(404, "Item not found")
        schema = DeliverySchema(many=False)
        return schema.jsonify(delivery)
