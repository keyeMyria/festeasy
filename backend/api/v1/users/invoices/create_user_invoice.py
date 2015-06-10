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
from backend.models import CartProduct, Invoice, InvoiceProduct


logger = logging.getLogger(__name__)

def _create_user_invoice(order):
    """ Creates an invoice given an order.
    """
    with db.session.no_autoflush:
        invoice = Invoice(order=order)
        
        for order_product in OrderProduct.query.filter(OrderProduct.order==order).all():
            invoice_product = InvoiceProduct(
                product=order_product.product,
                invoice=invoice,
                unit_price_rands=order_product.product.price_rands,
                quantity=order_product.quantity,
                )
            db.session.add(invoice_product)
        
        db.session.add(invoice)
        db.session.commit()
    return invoice

@api.route('/users/<int:user_id>/invoices', methods=['POST'])
@require_auth()
def create_user_invoice(authenticated_user, user_id):
    """ Creates an invoice for a user.
    """

    user = get_or_404(User, user_id)

    _create_user_invoice(user)

    invoices = Invoice.query.join(Order).join(User).all()

    return jsonify(message="Successfully created invoice for user.", user=user, invoices=invoices), 201
