from flask import Blueprint
from flask_restful import Api
from .address.routes import AddressResource, AddressItemResource
from .bakery.routes import BakeryResource, BakeryItemResource, BakeryDetailResource, ProductsByBakeryResource
from .bank.routes import BankResource, BankItemResource, BankDetailResource
from .cart.routes import CartResource, CartItemResource
from .delivery.routes import DeliveryResource, DeliveryItemResource
from .product.routes import ProductResource, ProductItemResource
from .purchase.routes import PurchaseResource, PurchaseItemResource
from .user.routes import UserResource, UserItemResource, UserLoginResource, UserRegisterResource


bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)
api.add_resource(AddressResource, "/addresses/")
api.add_resource(AddressItemResource, "/address/<address_id>")

api.add_resource(BankResource, "/banks/")
api.add_resource(BankItemResource, "/bank/<bank_id>")
api.add_resource(BankDetailResource, "/bank/<bank_id>/detail")

api.add_resource(BakeryResource, "/bakeries/")
api.add_resource(BakeryItemResource, "/bakery/<bakery_id>")
api.add_resource(BakeryDetailResource, "/bakery/<bakery_id>/detail")
api.add_resource(ProductsByBakeryResource, "/bakery/<bakery_id>/products")

api.add_resource(CartResource, "/carts/")
api.add_resource(CartItemResource, "/cart/<cart_id>")

api.add_resource(DeliveryResource, "/deliveries/")
api.add_resource(DeliveryItemResource, "/delivery/<delivery_id>")

api.add_resource(ProductResource, "/products/")
api.add_resource(ProductItemResource, "/product/<product_id>")

api.add_resource(PurchaseResource, "/purchases/")
api.add_resource(PurchaseItemResource, "/purchase/<purchase_id>")

api.add_resource(UserResource, "/users/")
api.add_resource(UserItemResource, "/user/<user_id>")
api.add_resource(UserLoginResource, "/login/")
api.add_resource(UserRegisterResource, "/register/")


def init_app(app):
    app.register_blueprint(bp)
