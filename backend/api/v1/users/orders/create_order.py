import datetime
import json
import logging
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.api.utils import get_or_404
from backend.api.v1.auth import require_auth
from backend.api.v1.forms import CreateUserCartProductsForm
from backend.api.v1.forms import CreateUserCartProductForm
from backend.models import User, UserCartProduct, Product
from backend.models import Order


logger = logging.getLogger(__name__)

def _create_order(user):
    """ Creates an order given a user.
    """
    order = Order()

    order.products = user.cart_products
    
    # TODO: why does the order of these two matter?
    order.event = user.current_cart_event
    order.user = user
    

    db.session.add(order)
    db.session.commit()
    return order

@api.route('/users/<int:user_id>/orders', methods=['POST'])
@require_auth()
def create_order(authenticated_user, user_id):
    """ Creates an order for a user.
    """

    user = get_or_404(User, user_id)

    _create_order(user)

    orders = Order.query.filter(Order.user==user).all()

    return jsonify(message="Successfully created order for user.", orders=orders), 201
