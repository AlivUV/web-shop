from flask import render_template

from server import app
from models import Product


@app.route('/product/get-all')
def get_all_products():
    all_products = Product.get_all()
    return render_template('products/get_all_products.html', products=all_products)