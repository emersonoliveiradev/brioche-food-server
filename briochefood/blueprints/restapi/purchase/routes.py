from flask import abort, jsonify
from flask_restful import Resource
from briochefood.models import Purchase


class PurchaseResource(Resource):
    def get(self):
        purchases = Purchase.query.all() or abort(204)
        return jsonify(
            {"purchases": [purchase.to_dict() for purchase in purchases]}
        )


class PurchaseItemResource(Resource):
    def get(self, purchase_id):
        purchase = Purchase.query.filter_by(
            id=purchase_id).first() or abort(404)
        return jsonify(purchase.to_dict())
