import datetime
import json
import logging
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.api.utils import get_or_404
from backend.api.auth import require_auth
from backend.api.forms import CreateUserCartProductsForm
from backend.api.forms import CreateUserCartProductForm
from backend.models import User, Product, CartProduct


logger = logging.getLogger(__name__)

def _create_user_cart_product(user, product):
    """ Creates a cart_product given a user 
    and a product.
    """
    cart_product = CartProduct(
        product=product,
        cart=user.cart,
        )
    db.session.add(cart_product)
    db.session.commit()
    return cart_product

@api.route('/users/<int:user_id>/cart/cart_products', methods=['POST'])
@require_auth()
def create_user_cart_product(user_id, authenticated_user):
    """ Creates a user_cart_product.
    """
    create_cart_product_form = CreateUserCartProductForm(**request.get_json())
    if not create_cart_product_form.validate():
        logger.warn("Failed to create cart products, form did not validate.")
        return jsonify(message="Failed to create cart products, form did not validate."), 400

    user = get_or_404(User, user_id)
    product_id = create_cart_product_form.product_id.data
    product = get_or_404(Product, product_id)

    _create_user_cart_product(user, product)
    return jsonify(message="Successfully created a cart_product.", cart=user.cart), 201

@api.route('/users/<int:user_id>/cart/cart_products/multiple', methods=['POST'])
@require_auth()
def create_user_cart_products(user_id, authenticated_user):
    """ Creates one or more user_cart_products.
    """
    create_cart_products_form = CreateUserCartProductsForm(**request.get_json())
    if not create_cart_products_form.validate():
        logger.warn("Failed to create cart products, form did not validate.")
        return jsonify(message="Failed to create cart products, form did not validate."), 400

    user = get_or_404(User, user_id)
    for item in create_cart_products_form.product_ids.data:
        product_id = item['product_id']
        product = get_or_404(Product, product_id)
        _create_user_cart_product(user, product)
    return jsonify(message="Successfully created cart_products.", cart=user.cart), 201
