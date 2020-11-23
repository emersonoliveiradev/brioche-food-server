from briochefood.ext.database import db
from sqlalchemy_serializer import SerializerMixin
import datetime


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    lastname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    cpf = db.Column(db.String(11), unique=True,)
    phone = db.Column(db.String(13))
    status = db.Column(db.String(20), db.Enum(
        'ACTIVE', 'BLOCKED'), default='ACTIVE', nullable=False)
    address = db.relationship("Address", secondary="users_addresses")
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=None)


class Address(db.Model, SerializerMixin):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(128))
    number = db.Column(db.Integer())
    complement = db.Column(db.String(128))
    district = db.Column(db.String(128))
    city = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    country = db.Column(db.String(128), default='Brasil', nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=None)
    user = db.relationship("User", secondary="users_addresses")


class User_Address(db.Model, SerializerMixin):
    __tablename__ = 'users_addresses'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey(
        'addresses.id'), nullable=False)
    user = db.relationship(User, backref=db.backref(
        "users_addresses", cascade="all, delete-orphan"))
    address = db.relationship(Address, backref=db.backref(
        "users_addresses", cascade="all, delete-orphan"))


class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    cnpj = db.Column(db.String(13), default=None, unique=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(13))
    status = db.Column(db.String(20), db.Enum(
        'ACTIVE', 'INACTIVE', 'BLOCKED'), default='ACTIVE', nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey(
        'addresses.id'), nullable=False)
    address = db.relationship("Address", backref="bakeries")

    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=None)


class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(), default=0)
    quantity = db.Column(db.Integer, default=0)
    status = db.Column(db.String(20), db.Enum(
        'ACTIVE', 'INACTIVE'), default='ACTIVE', nullable=False)
    bakery_id = db.Column(db.Integer, db.ForeignKey(
        'bakeries.id'), nullable=False)
    bakery = db.relationship("Bakery", backref="products")
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=None)


class Cart(db.Model, SerializerMixin):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(200))
    bakery_id = db.Column(db.Integer, db.ForeignKey(
        'bakeries.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=None)


class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.Numeric(), nullable=False)
    note = db.Column(db.String(200))
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=None)


class Purchase(db.Model, SerializerMixin):
    __tablename__ = 'purchases'
    id = db.Column(db.Integer, primary_key=True)
    total_paid = db.Column(db.Numeric(), nullable=False)
    bakery_received = db.Column(db.Numeric(), nullable=False)
    startup_received = db.Column(db.Numeric(), nullable=False)
    percentage_charged = db.Column(db.Numeric(), nullable=False)
    status = db.Column(db.String(20), db.Enum(
        'PAID', 'CANCELED', 'REVERSAL'), default='PAID', nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=None)


class Delivery(db.Model, SerializerMixin):
    __tablename__ = 'deliveries'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), db.Enum('PENDENT', 'CANCELED',
                                              'INPROGRESS', 'DELIVERED'), default='PENDENT', nullable=False)
    note = db.Column(db.String(200))
    purchase_id = db.Column(db.Integer, db.ForeignKey(
        'purchases.id'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey(
        'addresses.id'), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=None)
