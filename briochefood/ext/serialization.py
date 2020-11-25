from marshmallow import validate
from flask_marshmallow import Marshmallow
from briochefood.models import Address, Bakery, Bank, Cart, Product, Purchase, User

ma = Marshmallow()


def init_app(app):
    ma.init_app(app)


class AddressSchema(ma.Schema):
    class Meta:
        model = Address

    id = ma.Int()
    street = ma.Str(validate=validate.Length(max=128))
    number = ma.Int()
    complement = ma.Str(validate=validate.Length(max=128))
    district = ma.Str(validate=validate.Length(max=128))
    city = ma.Str(validate=validate.Length(max=128))
    state = ma.Str(required=True, validate=validate.Length(min=2, max=2))
    zipcode = ma.Str(required=True, validate=validate.Length(min=8, max=8))
    country = ma.Str(required=True, validate=validate.Length(max=128))
    created_at = ma.DateTime()
    updated_at = ma.DateTime()


class BankSchema(ma.Schema):
    class Meta:
        model = Bank

    id = ma.Int()
    pagarme_bank_account_id = ma.Str(validate=validate.Length(max=128))
    agencia = ma.Str(required=True, validate=validate.Length(
        max=5))
    agencia_dv = ma.Str(validate=validate.Length(max=1))
    bank_code = ma.Str(required=True, validate=validate.Length(max=3))
    conta = ma.Str(required=True, validate=validate.Length(max=13))
    conta_dv = ma.Str(
        required=True, validate=validate.Length(min=1, max=2))
    document_type = ma.Str(validate=validate.Length(max=30))
    document_number = ma.Str(
        required=True, validate=validate.Length(max=18))
    legal_name = ma.Str(
        required=True, validate=validate.Length(max=30))
    type = ma.Str(validate=validate.Length(max=30))
    charge_transfer_fees = ma.Boolean()
    created_at = ma.DateTime()
    updated_at = ma.DateTime()
    date_created = ma.Str()


class BakeryPagarmeRecipientSchema(ma.Schema):
    id = ma.Str()
    transfer_enabled = ma.Boolean()
    last_transfer = ma.Str()
    transfer_interval = ma.Str()
    transfer_day = ma.Int()
    automatic_anticipation_enabled = ma.Boolean()
    automatic_anticipation_type = ma.Str()
    automatic_anticipation_days = ma.Str()
    automatic_anticipation_1025_delay = ma.Int()
    anticipatable_volume_percentage = ma.Int()
    date_created = ma.Str()
    date_updated = ma.Str()
    bank_account = ma.Nested(BankSchema(), required=True)


class BakerySchema(ma.Schema):
    class Meta:
        model = Bakery

    id = ma.Int()
    pagarme_recipient_id = ma.Str(validate=validate.Length(max=128))
    name = ma.Str(required=True, validate=validate.Length(min=2, max=128))
    cnpj = ma.Str(validate=validate.Length(min=13, max=13))
    email = ma.Str(required=True, validate=validate.Length(min=2, max=128))
    phone = ma.Str(validate=validate.Length(min=13, max=13))
    status = ma.Str(validate=validate.Length(max=20))
    address_id = ma.Int()
    address = ma.Nested(AddressSchema(), required=True)
    bank = ma.Nested(BankSchema(), required=True)
    pagarme_recipient = ma.Nested(BakeryPagarmeRecipientSchema())
    created_at = ma.DateTime()
    updated_at = ma.DateTime()


class ProductSchema(ma.Schema):
    class Meta:
        model = Product

    id = ma.Int()
    title = ma.Str(required=True, validate=validate.Length(min=1, max=255))
    description = ma.Str()
    unit_price = ma.Float()
    quantity = ma.Int()
    tangible = ma.Boolean()
    status = ma.Str(validate=validate.Length(max=20))
    bakery_id = ma.Int()
    bakery = ma.Nested(BakerySchema())
    created_at = ma.DateTime()
    updated_at = ma.DateTime()


class UserSchema(ma.Schema):
    class Meta:
        model = User

    id = ma.Int()
    name = ma.Str(required=True, validate=validate.Length(min=2, max=128))
    lastname = ma.Str(required=True, validate=validate.Length(min=2, max=128))
    email = ma.Str(required=True, validate=validate.Length(min=2, max=128))
    password = ma.Str(required=True, validate=validate.Length(
        min=6, max=128))
    cpf = ma.Str(validate=validate.Length(min=11, max=11))
    phone = ma.Str(validate=validate.Length(min=13, max=13))
    birth_date = ma.DateTime()
    status = ma.Str(validate=validate.Length(max=20))
    type = ma.Str(validate=validate.Length(max=20))
    address = ma.Nested(AddressSchema(many=True))
    created_at = ma.DateTime()
    updated_at = ma.DateTime()


class CartSchema(ma.Schema):
    class Meta:
        model = Cart

    id = ma.Int()
    note = ma.Str()
    bakery_id = ma.Int(required=True)
    bakery = ma.Nested(BakerySchema())
    user_id = ma.Int()
    user = ma.Nested(UserSchema())
    created_at = ma.DateTime()
    updated_at = ma.DateTime()


class DeliverySchema(ma.Schema):
    class Meta:
        model = Address

    id = ma.Int()
    status = ma.Str(required=True, validate=validate.Length(max=20))
    note = ma.Str(validate=validate.Length(max=200))
    purchase_id = ma.Int(required=True)
    address_id = ma.Int(required=True)
    created_at = ma.DateTime()
    updated_at = ma.DateTime()


class LoginSchema(ma.Schema):
    class Meta:
        model = User

    email = ma.Str(required=True, validate=validate.Length(min=2, max=128))
    password = ma.Str(required=True, validate=validate.Length(
        min=6, max=128))


class CustomerSchema(ma.Schema):
    external_id = ma.Str(
        required=True, validate=validate.Length(min=1, max=128))
    name = ma.Str(required=True, validate=validate.Length(min=2, max=128))
    type = ma.Str(required=True, validate=validate.Length(min=2, max=128))
    country = ma.Str(required=True, validate=validate.Length(min=2, max=128))
    email = ma.Str(required=True, validate=validate.Length(min=2, max=128))
    documents = ma.Raw()
    phone_numbers = ma.Raw()
    birthday = ma.Str(required=True, validate=validate.Length(min=8, max=10))


class BillingShippingAddressSchema(ma.Schema):
    country = ma.Str(required=True, validate=validate.Length(max=128))
    state = ma.Str(required=True, validate=validate.Length(max=2))
    city = ma.Str(required=True, validate=validate.Length(max=128))
    neighborhood = ma.Str(required=True, validate=validate.Length(max=128))
    street = ma.Str(required=True, validate=validate.Length(max=128))
    street_number = ma.Str(required=True, validate=validate.Length(max=15))
    zipcode = ma.Str(validate=validate.Length(min=8, max=8))


class BillingSchema(ma.Schema):
    name = ma.Str(required=True, validate=validate.Length(max=128))
    address = ma.Nested(BillingShippingAddressSchema())


class ShippinSchema(ma.Schema):
    name = ma.Str(required=True, validate=validate.Length(max=128))
    fee = ma.Int(required=True,)
    delivery_date = ma.Str(
        required=True, validate=validate.Length(min=8, max=10))
    expedited = ma.Boolean()
    address = ma.Nested(BillingShippingAddressSchema())


class ItemsSchema(ma.Schema):
    id = ma.Str(required=True)
    title = ma.Str(required=True, validate=validate.Length(min=1, max=255))
    unit_price = ma.Int(required=True)
    quantity = ma.Int(required=True)
    tangible = ma.Boolean(required=True)


class PurchaseSchema(ma.Schema):
    class Meta:
        model = Purchase

    id = ma.Int()
    bakery_id = ma.Int()
    cart = ma.Nested(CartSchema())
    user_id = ma.Int()
    note = ma.Str(validate=validate.Length(max=128))
    amount = ma.Int(required=True,)
    card_number = ma.Str(
        required=True, validate=validate.Length(min=16, max=16))
    card_cvv = ma.Str(required=True, validate=validate.Length(min=1, max=3))
    card_expiration_date = ma.Str(
        required=True, validate=validate.Length(min=4, max=4))
    card_holder_name = ma.Str(
        required=True, validate=validate.Length(min=1, max=128))
    customer = ma.Nested(CustomerSchema())
    billing = ma.Nested(BillingSchema())
    shipping = ma.Nested(ShippinSchema())
    items = ma.Raw()
    split_rules = ma.Raw()
    created_at = ma.DateTime()
    updated_at = ma.DateTime()
