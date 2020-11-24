from flask import abort, current_app, jsonify
from flask_restful import Resource
from briochefood.models import Bank
from briochefood.ext.serialization import BankSchema

import pagarme


class BankResource(Resource):
    def get(self):
        """Get all banks"""
        banks = Bank.query.all() or abort(204, "No items found")
        schema = BankSchema(many=True)
        return schema.jsonify(banks)


class BankItemResource(Resource):
    def get(self, bank_id):
        """Get bank"""
        bank = Bank.query.filter_by(
            id=bank_id).first() or abort(404, "Item not found")
        schema = BankSchema(many=False)
        return schema.jsonify(bank)


class BankDetailResource(Resource):
    def get(self, bank_id):
        """Detail bank"""
        pagarme.authentication_key(
            current_app.config.get('PAGARME_API_KEY'))

        bank = Bank.query.filter_by(
            id=bank_id).first() or abort(404, "Item not found")
        bank = pagarme.bank_account.find_by(
            {"id": bank.pagarme_bank_account_id})

        schema = BankSchema(many=False)
        return schema.jsonify(bank[0]) if (len(bank) == 1) else abort(
            404, "Item not found"
        )
