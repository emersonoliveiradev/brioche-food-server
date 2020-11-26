from datetime import datetime
from flask import abort, current_app, jsonify
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required
from briochefood.ext.database import db
from briochefood.ext.serialization import PurchaseSchema
from briochefood.models import Bakery, Cart, Order, Product, Purchase, User
import pagarme


split_rules = [
    {
        "recipient_id": "re_ckhrqo2gs0f730h9tsqj4qupd",
        "percentage": 15,
        "liable": True,
        "charge_processing_fee": False
    }, {
        "recipient_id": "",
        "percentage": 85,
        "liable": False,
        "charge_processing_fee": True
    }
]


class PurchaseResource(Resource):
    @jwt_required
    def get(self):
        purchases = Purchase.query.all() or abort(204, "No items found")
        schema = PurchaseSchema(many=True)
        return schema.jsonify(purchases)

    def post(self):
        try:
            schema = PurchaseSchema()
            data = schema.load(request.get_json(force=True))

            bakery = Bakery.query.filter_by(
                id=data['bakery_id']).first() or abort(404, "Bakery not found")

            if data.get('user_id'):
                user = User.query.filter_by(
                    id=data['bakery_id']).first() or abort(404, "User not found")
                customer = {
                    "external_id": str(user.id),
                    "name": user.name + ' ' + user.lastname,
                    "type": "individual",
                    "country": "br",
                    "email": user.email,
                    "documents": [
                        {
                            "type": "cpf",
                            "number": user.cpf,
                        }
                    ],
                    "phone_numbers": ["+" + user.phone],
                    "birthday": user.birth_date.strftime('%Y-%m-%d')
                }

                billing = {
                    "name": user.name + ' ' + user.lastname,
                    "address": {
                        "country": user.address[0].country,
                        "state": user.address[0].state,
                        "city": user.address[0].city,
                        "neighborhood": user.address[0].district,
                        "street": user.address[0].street,
                        "street_number": str(user.address[0].number),
                        "zipcode": user.address[0].zipcode
                    }
                }

                shipping = {
                    "name": user.name + ' ' + user.lastname,
                    "fee": 0,
                    "delivery_date": datetime.now().strftime('%Y-%m-%d'),
                    "expedited": True,
                    "address": {
                        "country": user.address[0].country,
                        "state": user.address[0].state,
                        "city": user.address[0].city,
                        "neighborhood": user.address[0].district,
                        "street": user.address[0].street,
                        "street_number": str(user.address[0].number),
                        "zipcode": user.address[0].zipcode
                    }
                }

            cart = Cart(note=data.get('note', None),
                        bakery_id=data['bakery_id'],
                        user_id=data.get("user_id", None))
            db.session.add(cart)
            db.session.flush()

            items = []
            percentage_charged = 15
            amount = total_paid = bakery_received = startup_received = 0

            for item in data['items']:
                if item['quantity'] <= 0:
                    continue

                product = Product.query.filter_by(
                    id=item['id']).first() or abort(404, "Product not found")
                if product.quantity < item['quantity']:
                    abort(201, "The product does not have enough stock")
                items.append({
                    "id": str(product.id),
                    "title": product.title,
                    "unit_price": int(product.unit_price * 100),
                    "quantity": item['quantity'],
                    "tangible": product.tangible}
                )
                order = Order(quantity=item['quantity'],
                              unit_price=product.unit_price,
                              cart_id=cart.id, product_id=product.id)
                db.session.add(order)
                db.session.flush()

                total_paid += item['quantity'] * product.unit_price

            amount = int(total_paid * 100)
            bakery_received = total_paid * 85 / 100
            startup_received = total_paid - bakery_received

            split_rules[1]['recipient_id'] = bakery.pagarme_recipient_id

            if data.get('user_id'):
                purchase_pagarme = {
                    "amount": amount,
                    "card_number": data['card_number'],
                    "card_cvv": data['card_cvv'],
                    "card_expiration_date": data['card_expiration_date'],
                    "card_holder_name": data['card_holder_name'],
                    "items": items,
                    "split_rules": split_rules,
                    "customer": customer,
                    "billing": billing,
                    "shipping": shipping,
                }
            else:
                purchase_pagarme = {
                    "amount": amount,
                    "card_number": data['card_number'],
                    "card_cvv": data['card_cvv'],
                    "card_expiration_date": data['card_expiration_date'],
                    "card_holder_name": data['card_holder_name'],
                    "items": items,
                    "split_rules": split_rules,
                }

            pagarme.authentication_key(
                current_app.config.get('PAGARME_API_KEY'))
            trx = pagarme.transaction.create(purchase_pagarme)

            purchase = Purchase(total_paid=total_paid,
                                bakery_received=bakery_received,
                                startup_received=startup_received,
                                percentage_charged=percentage_charged,
                                status='PAID',
                                cart_id=cart.id)

            db.session.add(purchase)
            db.session.flush()
            db.session.commit()

            return schema.jsonify(purchase)
        except Exception as e:
            db.session.rollback()
            abort(400, "Registration not performed. " + str(e))


class PurchaseItemResource(Resource):
    @jwt_required
    def get(self, purchase_id):
        purchase = Purchase.query.filter_by(
            id=purchase_id).first() or abort(404, "Item not found")
        return jsonify(purchase.to_dict())
