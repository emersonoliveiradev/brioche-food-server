from flask import abort, jsonify
from flask_restful import Resource
from briochefood.models import Bakery


class BakeryResource(Resource):
    def get(self):
        bakeries = Bakery.query.all() or abort(204)
        return jsonify({"bakeries": [bakery.to_dict() for bakery in bakeries]})


class BakeryItemResource(Resource):
    def get(self, bakery_id):
        bakery = Bakery.query.filter_by(id=bakery_id).first() or abort(404)
        return jsonify(bakery.to_dict())
