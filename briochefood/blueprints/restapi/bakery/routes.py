from briochefood.blueprints.restapi import bank
from flask import abort, current_app
from flask_restful import Resource, request
from briochefood.models import Bakery
from briochefood.ext.database import db
from briochefood.ext.serialization import BakerySchema
import pagarme


class BakeryResource(Resource):
    def get(self):
        """Get all bakeries"""
        bakeries = Bakery.query.all() or abort(204)
        schema = BakerySchema(many=True)
        return schema.jsonify(bakeries)

    def post(self):
        """Create a new bakery"""
        try:
            pagarme.authentication_key(
                current_app.config.get('PAGARME_API_KEY'))
            schema = BakerySchema()
            data = schema.load(request.get_json(force=True))
            recipient = {
                'anticipatable_volume_percentage': '80',
                'automatic_anticipation_enabled': 'true',
                'transfer_day': '5',
                'transfer_enabled': 'true',
                'transfer_interval': 'weekly',
                'bank_account': data['bank']
            }

            rec = pagarme.recipient.create(recipient)
            return rec
            '''bakery = Bakery(name=data['name'], cnpj=data['cnpj'],
                            email=data['email'], password=data['password'],
                            address_id=2)
            db.session.add(bakery)
            db.session.commit()'''
            return schema.jsonify(bakery)
        except Exception as e:
            abort(400, "Registration not performed. " + str(e))


class BakeryItemResource(Resource):
    def get(self, bakery_id):
        """Get bakery"""
        bakery = Bakery.query.filter_by(id=bakery_id).first() or abort(404)
        schema = BakerySchema(many=False)
        return schema.jsonify(bakery)
