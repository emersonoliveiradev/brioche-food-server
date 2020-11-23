from flask import abort
from flask_restful import Resource
from briochefood.models import Bank
from briochefood.ext.serialization import BankSchema


class BankResource(Resource):
    def get(self):
        """Get all bakeries"""
        banks = Bank.query.all() or abort(204)
        schema = BankSchema(many=True)
        return schema.jsonify(banks)


class BankItemResource(Resource):
    def get(self, bank_id):
        """Get bank"""
        bank = Bank.query.filter_by(id=bank_id).first() or abort(404)
        schema = BankSchema(many=False)
        return schema.jsonify(bank)
