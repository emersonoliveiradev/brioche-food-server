from flask import abort, current_app
from flask_restful import Resource, request
from briochefood.ext.database import db
from briochefood.ext.serialization import BakerySchema
from briochefood.models import Address, Bakery, Bank

import pagarme


class BakeryResource(Resource):
    def get(self):
        """Get all bakeries"""
        bakeries = Bakery.query.all() or abort(204, "No items found")
        schema = BakerySchema(many=True)
        return schema.jsonify(bakeries)

    def post(self):
        """Create a new bakery"""
        try:
            pagarme.authentication_key(
                current_app.config.get('PAGARME_API_KEY'))

            schema = BakerySchema()

            data = schema.load(request.get_json(force=True))

            address = Address(
                street=data['address'].get("street", None),
                number=data['address'].get("number", None),
                complement=data['address'].get("complement", None),
                district=data['address'].get("district", None),
                city=data['address'].get("city", None),
                cep=data['address']['cep'],
                state=data['address']['state'],
                country=data['address']['country'],
            )
            db.session.add(address)
            db.session.flush()

            recipient = {
                'anticipatable_volume_percentage': '80',
                'automatic_anticipation_enabled': 'true',
                'transfer_day': '5',
                'transfer_enabled': 'true',
                'transfer_interval': 'weekly',
                'bank_account': data['bank']
            }
            recipient = pagarme.recipient.create(recipient) or abort(
                400, 'Bank data denied. Check your data.'
            )

            bank = Bank(
                pagarme_bank_account_id=recipient['bank_account']['id'])
            db.session.add(bank)
            db.session.flush()

            bakery = Bakery(pagarme_recipient_id=recipient['id'],
                            name=data['name'], cnpj=data['cnpj'],
                            email=data['email'], password=data['password'],
                            bank_id=bank.id,
                            address_id=address.id) or abort(
                400, 'Bakery data denied. Check your data.'
            )

            db.session.add(bakery)
            db.session.flush()

            db.session.commit()

            return schema.jsonify(bakery)
        except Exception as e:
            db.session.rollback()
            abort(400, "Registration not performed. " + str(e))


class BakeryItemResource(Resource):
    def get(self, bakery_id):
        """Get bakery"""
        bakery = Bakery.query.filter_by(
            id=bakery_id).first() or abort(404, "Item not found")
        schema = BakerySchema(many=False)
        return schema.jsonify(bakery)
