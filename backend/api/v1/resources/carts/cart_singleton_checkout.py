from flask_restful import Resource

from backend import db
from backend.models import Cart, Order, Invoice
from backend.api.utils import get_or_404
from backend.api.v1.exceptions import APIException


class CartSingletonCheckout(Resource):
    def post(self, cart_id):
        cart = get_or_404(Cart, Cart.id == cart_id)
        if not cart.festival:
            raise APIException(
                status_code=400,
                message="Cart needs a Festival."
            )
        if cart.products == []:
            raise APIException(
                status_code=400,
                message="Cart needs some Products."
            )
        order = Order.from_cart(cart)
        cart.products = []
        cart.festival = None
        db.session.add(cart)
        db.session.add(order)
        db.session.commit()
        # TODO: Sort out issue with flushing (Or something)
        invoice = Invoice.from_order(order)
        db.session.add(invoice)
        db.session.commit()
