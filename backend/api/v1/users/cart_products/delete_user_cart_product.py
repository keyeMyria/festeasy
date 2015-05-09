import datetime
import json
import logging
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.api.utils import get_or_404
from backend.api.v1.auth import require_auth
from backend.api.v1.forms import DeleteUserCartProductForm
from backend.models import User, UserCartProduct, Product


logger = logging.getLogger(__name__)

@api.route('/users/<int:user_id>/cart_products', methods=['DELETE'])
@require_auth()
def delete_user_cart_product(user_id, authenticated_user):
    delete_user_cart_product_form = DeleteUserCartProductForm(**request.get_json())
    if not delete_user_cart_product_form.validate():
        logger.warn("Failed to delete users cart products, form did not validate.")
        return jsonify(message="Failed to delete users cart products, form did not validate."), 401

    user = get_or_404(User, user_id)
    for item in delete_user_cart_product_form.user_cart_product_ids.data:
        user_cart_product_id = item['user_cart_product_id']
        user_cart_product = get_or_404(UserCartProduct, user_cart_product_id)
        db.session.delete(user_cart_product)
    db.session.commit()

    cart_products = UserCartProduct.query.filter(UserCartProduct.user==user).all()
    dumpable_list = list()
    for card_product in cart_products:
        dumpable_list.append(card_product.dump())
    return jsonify(message="Successfully created card_product.", cart_products=dumpable_list), 201
