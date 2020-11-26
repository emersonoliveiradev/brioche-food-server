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
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String(20), db.Enum(
        'CUSTOMER', 'EMPLOYE', 'OWNER'), default='CUSTOMER', nullable=False)
    bakery_id = db.Column(db.Integer, db.ForeignKey(
        'bakeries.id'), default=None)
    bakery = db.relationship("Bakery", backref="users")
    status = db.Column(db.String(20), db.Enum(
        'ACTIVE', 'BLOCKED'), default='ACTIVE', nullable=False)
    address = db.relationship("Address", secondary="users_addresses")
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=None)

    def __repr__(self):
        return '{} - {}'.format(self.id, self.name)


class Address(db.Model, SerializerMixin):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(128), nullable=False)
    number = db.Column(db.Integer(), nullable=False)
    complement = db.Column(db.String(128), nullable=False)
    district = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zipcode = db.Column(db.String(8), nullable=False)
    country = db.Column(db.String(2), default='br', nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=None)
    user = db.relationship("User", secondary="users_addresses")

    def __repr__(self):
        return '{}'.format(self.id)


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

    def __repr__(self):
        return '{}'.format(self.id)


class Bank(db.Model, SerializerMixin):
    __tablename__ = 'banks'
    id = db.Column(db.Integer, primary_key=True)
    pagarme_bank_account_id = db.Column(
        db.String(128), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=None)

    def __repr__(self):
        return '{} - {}'.format(self.id, self.pagarme_bank_account_id)


class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'
    id = db.Column(db.Integer, primary_key=True)
    pagarme_recipient_id = db.Column(
        db.String(128), nullable=False, unique=True)
    name = db.Column(db.String(128), nullable=False)
    cnpj = db.Column(db.String(13), default=None, unique=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    phone = db.Column(db.String(13))
    status = db.Column(db.String(20), db.Enum(
        'ACTIVE', 'INACTIVE', 'BLOCKED'), default='ACTIVE', nullable=False)
    bank_id = db.Column(db.Integer, db.ForeignKey(
        'banks.id'), unique=True, nullable=False)
    bank = db.relationship("Bank", backref="bakeries")
    address_id = db.Column(db.Integer, db.ForeignKey(
        'addresses.id'), nullable=False)
    address = db.relationship("Address", backref="bakeries")
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=None)

    def __repr__(self):
        return '{} - {}'.format(self.id, self.name)


class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225), nullable=False)
    description = db.Column(db.Text)
    unit_price = db.Column(db.Numeric(), default=0)
    quantity = db.Column(db.Integer, default=0)
    tangible = db.Column(db.Boolean, default=True, nullable=False)
    status = db.Column(db.String(20), db.Enum(
        'ACTIVE', 'INACTIVE'), default='ACTIVE', nullable=False)
    bakery_id = db.Column(db.Integer, db.ForeignKey(
        'bakeries.id'), nullable=False)
    bakery = db.relationship("Bakery", backref="products")
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=None)

    def __repr__(self):
        return '{} - {}'.format(self.id, self.title)


class Cart(db.Model, SerializerMixin):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(200))
    bakery_id = db.Column(db.Integer, db.ForeignKey(
        'bakeries.id'), nullable=False)
    bakery = db.relationship("Bakery", backref="carts")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", backref="carts")
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=None)

    def __repr__(self):
        return '{}'.format(self.id)


class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer(), nullable=False)
    unit_price = db.Column(db.Numeric(), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=None)

    def __repr__(self):
        return '{}'.format(self.id)


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
    cart = db.relationship("Cart", backref="purchases")
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=None)

    def __repr__(self):
        return '{}'.format(self.id)


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

    def __repr__(self):
        return '{}'.format(self.id)
