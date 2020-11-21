from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_simplelogin import login_required

from briochefood.ext.database import db
from briochefood.models import Address, Product, Purchase, User


AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)
admin = Admin()

def init_app(app):
    admin.name = app.config.TITLE
    admin.template_mode = "bootstrap3"
    admin.init_app(app)
    admin.add_view(sqla.ModelView(Address, db.session))
    admin.add_view(sqla.ModelView(Product, db.session))
    admin.add_view(sqla.ModelView(Purchase, db.session))
    admin.add_view(sqla.ModelView(User, db.session))
    
    