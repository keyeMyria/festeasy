import datetime
import json
import logging
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.api.utils import get_or_404
from backend.api.v1.auth import require_auth
from backend.api.v1.forms import CreateUserCartProductsForm
from backend.models import User, UserCartProduct, Product


logger = logging.getLogger(__name__)

def _create_user_cart_product(user, product):
    """ Creates a user_cart_product given a user 
    and a product.
    """
    user_cart_product = UserCartProduct()
    user_cart_product.user = user
    user_cart_product.product = product
    db.session.add(user_cart_product)
    db.session.commit()
    return user_cart_product

@api.route('/users/<int:user_id>/cart_products/multiple', methods=['POST'])
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
        product = get_or_404(Product, item['product_id'])
        _create_user_cart_product(user, product)

    user_cart_products = UserCartProduct.query.filter(UserCartProduct.user==user).all()
    return jsonify(message="Successfully created card_products.", user_cart_products=user_cart_products), 201
