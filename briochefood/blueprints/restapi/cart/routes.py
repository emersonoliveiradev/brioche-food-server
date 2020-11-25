from flask import abort
from flask_restful import Resource, request
from briochefood.models import Cart
from briochefood.ext.database import db
from briochefood.ext.serialization import CartSchema


class CartResource(Resource):
    def get(self):
        """Get all carts"""
        carts = Cart.query.all() or abort(204, "No items found")
        schema = CartSchema(many=True)
        return schema.jsonify(carts)

    def post(self):
        """Create a new cart"""
        try:
            schema = CartSchema()
            data = schema.load(request.get_json(force=True))

            cart = Cart(note=data.get('note', None),
                        bakery_id=data['bakery_id'],
                        user_id=data.get("user_id", None))

            db.session.add(cart)
            db.session.commit()
            return schema.jsonify(cart)
        except Exception as e:
            abort(400, "Registration not performed. " + str(e))


class CartItemResource(Resource):
    def get(self, cart_id):
        """Get cart"""
        cart = Cart.query.filter_by(
            id=cart_id).first() or abort(404, "Item not found")
        schema = CartSchema(many=False)
        return schema.jsonify(cart)
