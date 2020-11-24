from marshmallow import validate, ValidationError
from flask_marshmallow import Marshmallow
from briochefood.models import Address, Bakery, Bank, Product, User

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
    cep = ma.Str(required=True, validate=validate.Length(min=8, max=8))
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


class BakerySchema(ma.Schema):
    class Meta:
        model = Bakery

    id = ma.Int()
    pagarme_recipient_id = ma.Str(validate=validate.Length(max=128))
    name = ma.Str(required=True, validate=validate.Length(min=2, max=128))
    cnpj = ma.Str(validate=validate.Length(min=13, max=13))
    email = ma.Str(required=True, validate=validate.Length(min=2, max=128))
    password = ma.Str(required=True, validate=validate.Length(
        min=6, max=128), message="asdasd")
    phone = ma.Str(validate=validate.Length(min=13, max=13))
    status = ma.Str(validate=validate.Length(max=20))
    address_id = ma.Int()
    address = ma.Nested(AddressSchema(), required=True)
    bank = ma.Nested(BankSchema(), required=True)
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
    cpf = ma.Str(validate=validate.Length(min=11, max=11))
    status = ma.Str(validate=validate.Length(max=20))
    phone = ma.Str(validate=validate.Length(min=13, max=13))
    address = ma.Nested(AddressSchema(many=True))
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
