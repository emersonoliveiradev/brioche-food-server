from flask import abort
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required
from briochefood.models import Product
from briochefood.ext.database import db
from briochefood.ext.serialization import ProductSchema


class ProductResource(Resource):
    def get(self):
        """Get all products"""
        products = Product.query.all() or abort(204, "No items found")
        schema = ProductSchema(many=True)
        return schema.jsonify(products)

    @jwt_required
    def post(self):
        """Create a new product"""
        try:
            schema = ProductSchema()
            data = schema.load(request.get_json(force=True))
            product = Product(title=data['title'],
                              unit_price=data.get("unit_price", None),
                              description=data.get("description", None),
                              quantity=data.get("quantity", None),
                              tangible=data.get('tangible', None),
                              bakery_id=data['bakery_id'])
            db.session.add(product)
            db.session.commit()
            return schema.jsonify(product)
        except Exception as e:
            abort(400, "Registration not performed. " + str(e))


class ProductItemResource(Resource):
    def get(self, product_id):
        """Get product"""
        product = Product.query.filter_by(
            id=product_id).first() or abort(404, "Item not found")
        schema = ProductSchema(many=False)
        return schema.jsonify(product)
