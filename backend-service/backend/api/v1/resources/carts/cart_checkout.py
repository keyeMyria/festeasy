import datetime
from flask_restful import Resource

from backend import db
from backend.models import Cart, Order, Invoice
from backend.api.utils import get_or_404
from backend.api.v1.schemas import OrderSchema
from backend.exceptions import APIException
from backend.api.v1.authentication import requires_auth


class CartCheckout(Resource):
    method_decorators = [requires_auth]

    # TODO: Assert auth_user == cart.user
    def post(self, cart_id, authenticated_user):
        cart = get_or_404(Cart, Cart.id == cart_id)
        if not cart.festival:
            raise APIException(
                status_code=400,
                message="Cart needs a Festival."
            )
        now = datetime.datetime.now()
        # TODO: Abstract.
        if cart.festival.starts_on < now + datetime.timedelta(days=7):
            raise APIException(
                status_code=400,
                message="Festival starts too soon."
            )
        if not cart.cart_products:
            raise APIException(
                status_code=400,
                message="Cart needs some products."
            )
        order = Order.from_cart(cart)
        cart.cart_products = []
        cart.festival = None
        db.session.add(cart)
        db.session.add(order)
        db.session.flush()
        invoice = Invoice.from_order(order)
        db.session.add(invoice)
        db.session.commit()
        return OrderSchema().dump(order).data
