from flask import flash, render_template, redirect, url_for
from flask_login import login_required
from forms import UpdateProductForm

from decorators import admin_required
from models import Product
from server import app

@app.route('/admin/update-product/<int:id>', methods=['GET', 'POST'])
# @login_required
# @admin_required
def update_product(id):
    form = UpdateProductForm()
    product = Product.get_by_id(id)
    error = ''
    success = ''
    if not product.is_active:
        form.is_active.label.text = 'Enable product'
    if form.validate_on_submit():
        if form.is_active.data:
            product.update_active(not product.is_active)
            success = 'The product has been updated'
            flash(success, 'success')
        elif form.submit.data:
            product_data = {
                'price': form.price.data
            }
            product.update_price(product_data['price'])
            success = 'Product updated successfully.'
            flash(success, 'success')
        else:
            '' 
        return redirect(url_for('get_all_products'))
    return render_template('admin/update_product.html', form=form, error=error, success=success, old_data=product)