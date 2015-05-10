import datetime
import json
import logging
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.api.utils import get_or_404
from backend.api.v1.auth import require_auth
from backend.api.v1.forms import DeleteUserCartProductsForm
from backend.models import User, UserCartProduct, Product


logger = logging.getLogger(__name__)

@api.route('/users/<int:user_id>/cart_products/multiple', methods=['DELETE'])
@require_auth()
def delete_user_cart_products(user_id, authenticated_user):
    print(request.args)
    user_cart_product_ids = request.args.get('user_cart_product_ids').split(',')
    if not user_cart_product_ids:
        logger.warn("No IDs to delete.")
        return jsonify(message="No IDs to delete."), 400

    user = get_or_404(User, user_id)
    for user_cart_product_id in user_cart_product_ids:
        user_cart_product = get_or_404(UserCartProduct, user_cart_product_id)
        db.session.delete(user_cart_product)
    db.session.commit()

    cart_products = UserCartProduct.query.filter(UserCartProduct.user==user).all()
    dumpable_list = list()
    for card_product in cart_products:
        dumpable_list.append(card_product.dump())
    return jsonify(message="Successfully created card_product.", cart_products=dumpable_list), 201
