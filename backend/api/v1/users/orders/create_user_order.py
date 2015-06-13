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
from backend.models import Invoice


logger = logging.getLogger(__name__)

def _create_user_invoice(order):
    invoice = Invoice()
    invoice.from_order(order)
    return invoice

def _create_user_order(cart):
    """ Creates an order with an invoice given a cart.
    """
    order = Order()
    order.from_cart(cart)
    db.session.add(order)
    db.session.commit()
    # TODO: There is an issue with cascade on products and order_products
    # order has to be commited before invoice can be created.
    invoice = _create_user_invoice(order)
    db.session.add(invoice)
    db.session.commit()
    return order

@api.route('/users/<int:user_id>/orders', methods=['POST'])
@require_auth()
def create_user_order(authenticated_user, user_id):
    """ Creates an order with an invoice for a user.
    """

    user = get_or_404(User, user_id)

    if not user.cart.event:
        logger.warn("Failed to create order, no current_cart_event selected.")
        return jsonify(message="Failed to create order, no current_cart_event selected."), 400

    _create_user_order(user.cart)

    orders = Order.query.filter(Order.user==user).all()

    return jsonify(message="Successfully created order for user.", orders=orders), 201
