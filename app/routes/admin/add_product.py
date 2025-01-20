from flask import render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from forms import AddProductForm

from decorators import admin_required
from models import Product
from server import app

@app.route('/admin/add-product', methods=['GET', 'POST'])
@login_required
@admin_required
def add_product():
    form = AddProductForm()
    error = ''
    success = ''
    if form.validate_on_submit():
        product_data = {
            'name': form.name.data,
            'description': form.description.data,
            'stock': form.stock.data,
            'price': form.price.data
        }
        product = Product.get_by_name(product_data['name'])
        if product is not None:
            error = 'This product already exists.'
        else:
            product = Product.create_product(**product_data)
            success = 'Product added successfully.'
    return render_template('admin/add_product.html', form=form, error=error, success=success)