import datetime
import json
import logging
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.api.utils import get_or_404
from backend.api.auth import require_auth
from backend.models import User, Product, CartProduct


logger = logging.getLogger(__name__)

@api.route('/users/<int:user_id>/cart_products/multiple', methods=['DELETE'])
@require_auth()
def delete_user_cart_products(user_id, authenticated_user):
    """ Deletes one or more user_cart_products based on 
    query parameters.
    """
    cart_product_ids = request.args.get('cart_product_ids').split(',')
    if not cart_product_ids:
        logger.warn("No cart_product IDs to delete.")
        return jsonify(message="No cart_product IDs to delete."), 400

    user = get_or_404(User, user_id)
    for cart_product_id in cart_product_ids:
        cart_product = get_or_404(CartProduct, cart_product_id)
        db.session.delete(cart_product)
    db.session.commit()

    return jsonify(message="Successfully deleted cart_products.", cart=user.cart), 201
