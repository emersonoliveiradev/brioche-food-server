from flask import render_template, abort
from briochefood.models import Product


def index():
    products = Product.query.all()
    return render_template("index.html", products=products)


def product(product_id):
    product = Product.query.filter_by(
        id=product_id).first() or abort(404, "Item not found")
    return render_template("product.html", product=product)
