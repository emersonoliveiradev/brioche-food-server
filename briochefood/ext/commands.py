from briochefood.ext.database import db
#from briochefood.ext.auth import create_user
from briochefood.models import Address, Bakery, Cart, Delivery, Order, Product, Purchase, User, User_Address
from datetime import datetime

def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        Address(id=1, street='Gonçalo Carvalho', number= 33, complement='Apartamento', district='Floresta', city='Porto Alegre', cep='90035170', state='RS', country='Brasil', created_at=datetime.now(), updated_at=None),
        Address(id=2, street='Gonçalo Carvalho', number= 66, complement='Apartamento', district='Floresta', city='Porto Alegre', cep='90035170', state='RS', country='Brasil', created_at=datetime.now(), updated_at=None),
        Bakery(id=1, name='Pão Dourado', cnpj='1234567890123', email='paodourado@gmail.com', password='12345', status='ACTIVE', address_id='1', created_at=datetime.now(), updated_at=None),
        Bakery(id=2, name='Sonho da Manhã', cnpj='1234567891234', email='sonhodamanha@gmail.com', password='12345', status='ACTIVE', address_id='1', created_at=datetime.now(), updated_at=None),
        Product(id=1, name='Pão Francês', description='Pão comum a base de farinha, sal, água e fermento.', price=0.65, quantity= 120, status='ACTIVE', bakery_id= 1, created_at=datetime.now(), updated_at=None),
        Product(id=2, name='Pão Doce', description='Pão doce de textura macia e sabor de canela.', price=0.85, quantity= 90, status='ACTIVE', bakery_id= 1, created_at=datetime.now(), updated_at=None),        
        Product(id=3, name='Pão Francês', description='Pão comum a base de farinha, sal, água e fermento.', price=0.65, quantity= 120, status='ACTIVE', bakery_id= 2, created_at=datetime.now(), updated_at=None),        
        Product(id=4, name='Pão Doce Especial', description='Pão doce de textura macia e sabor de canela com geléia.', price=0.65, quantity= 120, status='ACTIVE', bakery_id= 1, created_at=datetime.now(), updated_at=None),
        User(id=1, name='Emerson', lastname='Oliveira', email='emersonoliveiradev@gmail.com', password="12345", cpf="21496453000", phone='5538998411815', status='ACTIVE', created_at=datetime.now(), updated_at=None),
        User_Address(user_id=1, address_id=2),
        User(id=2, name='Amelia', lastname='Brand', email='ameliabrand@gmail.com', password="12345", phone='5538998411815', status='ACTIVE', created_at=datetime.now(), updated_at=None),
        User_Address(user_id=2, address_id=2),
        User(id=3, name='Joseph', lastname='Cooper', email='josephcooper@gmail.com', password="12345", phone='5538998411815', status='ACTIVE', created_at=datetime.now(), updated_at=None),        
        Cart(id=1, note='Prioridade máxima na entrega por favor', bakery_id=1, user_id=1, created_at=datetime.now(), updated_at=None),
        Order(id=1, quantity=10, price=6.5, product_id=1, cart_id=1, created_at=datetime.now(), updated_at=None),        
        Order(id=2, quantity=8, price=6.8, product_id=2, cart_id=1, created_at=datetime.now(), updated_at=None),
        Purchase(id=1, total_paid=13.3, bakery_received=11.3, startup_received=2.0, percentage_charged=15.0, status='PAID', cart_id=1, created_at=datetime.now(), updated_at=None),
        Delivery(id=1, note="Pode deixar na portaria.", address_id=1, purchase_id=1, created_at=datetime.now(), updated_at=None),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Address.query.all()


def init_app(app):
    """Add multiple commands in a bulk"""
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))    