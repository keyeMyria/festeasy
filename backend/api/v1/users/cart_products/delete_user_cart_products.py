import datetime
import json
import logging
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.api.utils import get_or_404
from backend.api.auth import require_auth
from backend.models import User, UserCartProduct, Product


logger = logging.getLogger(__name__)

@api.route('/users/<int:user_id>/cart_products/multiple', methods=['DELETE'])
@require_auth()
def delete_user_cart_products(user_id, authenticated_user):
    """ Deletes one or more user_cart_products based on 
    query parameters.
    """
    user_cart_product_ids = request.args.get('user_cart_product_ids').split(',')
    if not user_cart_product_ids:
        logger.warn("No user_cart_product IDs to delete.")
        return jsonify(message="No user_cart_product IDs to delete."), 400

    user = get_or_404(User, user_id)
    for user_cart_product_id in user_cart_product_ids:
        user_cart_product = get_or_404(UserCartProduct, user_cart_product_id)
        db.session.delete(user_cart_product)
    db.session.commit()

    user_cart_products = UserCartProduct.query.filter(UserCartProduct.user==user).all()
    return jsonify(message="Successfully deleted user_cart_products.", user_cart_products=user_cart_products), 201
