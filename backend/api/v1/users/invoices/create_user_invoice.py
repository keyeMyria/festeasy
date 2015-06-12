import datetime
import json
import logging
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.api.utils import get_or_404
from backend.api.auth import require_auth
from backend.api.forms import CreateUserInvoiceForm
from backend.models import User
from backend.models import Order
from backend.models import Invoice


logger = logging.getLogger(__name__)

def _create_user_invoice(order):
    """ Creates an invoice given an order.
    """
    invoice = Invoice()
    invoice.from_order(order)
    db.session.add(invoice)
    db.session.commit()
    return invoice

@api.route('/users/<int:user_id>/invoices', methods=['POST'])
@require_auth()
def create_user_invoice(authenticated_user, user_id):
    """ Creates an invoice for a user.
    """
    user = get_or_404(User, user_id) 
    create_user_invoice_form = CreateUserInvoiceForm(**request.get_json())
    order_id = create_user_invoice_form.order_id.data
    order = get_or_404(Order, order_id)
    invoice = _create_user_invoice(order)
    invoices = Invoice.query.join(Order).join(User).all()

    return jsonify(message="Successfully created invoice for user.", invoice=invoice, invoices=invoices), 201
