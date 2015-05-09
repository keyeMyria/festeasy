import datetime
import json
import logging
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.api.utils import get_or_404
from backend.api.v1.auth import require_auth
from backend.api.v1.forms import CreateUserCartProductForm
from backend.models import User, UserCartProduct, Product


logger = logging.getLogger(__name__)

@api.route('/users/<int:user_id>/cart_products', methods=['POST'])
@require_auth()
def create_user_cart_product(user_id, authenticated_user):
    create_cart_product_form = CreateUserCartProductForm(**request.get_json())
    if not create_cart_product_form.validate():
        logger.warn("Failed to create cart products, form did not validate.")
        return jsonify(message="Failed to create cart products, form did not validate."), 401

    user = get_or_404(User, user_id)
    for item in create_cart_product_form.product_ids.data:
        product_id = item['product_id']
        product = get_or_404(Product, product_id)
        user_product_cart = UserCartProduct()
        user_product_cart.user = user
        user_product_cart.product = product
        db.session.add(user_product_cart)
    db.session.commit()

    cart_products = UserCartProduct.query.filter(UserCartProduct.user==user).all()
    dumpable_list = list()
    for card_product in cart_products:
        dumpable_list.append(card_product.dump())
    return jsonify(message="Successfully created card_product.", cart_products=dumpable_list), 201
