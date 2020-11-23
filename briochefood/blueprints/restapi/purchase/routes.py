from flask import abort, current_app, jsonify
from flask_restful import Resource, request
from briochefood.models import Purchase
import pagarme


class PurchaseResource(Resource):
    def get(self):
        purchases = Purchase.query.all() or abort(204)
        return jsonify(
            {"purchases": [purchase.to_dict() for purchase in purchases]}
        )

    def post(self):
        pagarme.authentication_key(current_app.config.get('PAGARME_API_KEY'))
        data = request.get_json(force=True) or abort(400, "Invalid request")
        trx = pagarme.transaction.create(data)
        return jsonify({"Checkout": trx})


class PurchaseItemResource(Resource):
    def get(self, purchase_id):
        purchase = Purchase.query.filter_by(
            id=purchase_id).first() or abort(404)
        return jsonify(purchase.to_dict())
