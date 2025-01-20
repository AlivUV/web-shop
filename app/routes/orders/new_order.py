from flask import render_template, redirect, request, url_for
from flask_login import login_required, current_user
from forms import SignupForm

from models import Product
from server import app

@app.route('/order/new-order', methods=['GET', 'POST'])
@login_required
def create_order():
    form = SignupForm()

    if request.method == 'POST':
        product = request.form['select_product']
        quantity = request.form['quantity']

    products = Product.get_all()

    return render_template('orders/create_order.html', form=form, products=products)