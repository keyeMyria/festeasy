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
from backend.models import User, Product
from backend.models import Order, OrderProduct
from backend.models import CartProduct


logger = logging.getLogger(__name__)

def _create_user_order(user):
    """ Creates an order given a user.
    """
    with db.session.no_autoflush:
        order = Order(create_from_cart=True, user=user)

        db.session.add(order)
        db.session.commit()
    return order

@api.route('/users/<int:user_id>/orders', methods=['POST'])
@require_auth()
def create_user_order(authenticated_user, user_id):
    """ Creates an order for a user.
    """

    user = get_or_404(User, user_id)

    if not user.cart.event:
        logger.warn("Failed to create order, no current_cart_event selected.")
        return jsonify(message="Failed to create order, no current_cart_event selected."), 400

    _create_user_order(user)

    orders = Order.query.filter(Order.user==user).all()

    return jsonify(message="Successfully created order for user.", user=user, orders=orders), 201
