import datetime
import json
import logging
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.api.utils import get_or_404
from backend.api.auth import require_auth
from backend.api.forms import CreateUserInvoiceForm
from backend.models import User, Product
from backend.models import Order, OrderProduct
from backend.models import CartProduct, Invoice, InvoiceProduct


logger = logging.getLogger(__name__)

def _create_user_invoice(order):
    """ Creates an invoice given an order.
    """
    with db.session.no_autoflush:
        invoice = Invoice(create_from_order=True, order=order)
        
        db.session.add(invoice)
        db.session.commit()
    return invoice

@api.route('/users/<int:user_id>/invoices', methods=['POST'])
@require_auth()
def create_user_invoice(authenticated_user, user_id):
    """ Creates an invoice for a user.
    """

    create_user_invoice_form = CreateUserInvoiceForm(**request.get_json())
    order_id = create_user_invoice_form.order_id.data

    order = get_or_404(Order, order_id)

    user = get_or_404(User, user_id)

    _create_user_invoice(user)

    invoices = []

    return jsonify(message="Successfully created invoice for user.", user=user), 201
