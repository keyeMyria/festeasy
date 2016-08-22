import datetime
from flask import request
from flask_restful import Resource

from backend import db
from backend.tasks import send_templated_email
from backend.models import Cart, Order, Invoice
from backend.api.utils import get_or_404
from backend.api.v1.schemas import OrderSchema, CartCheckoutSchema
from backend.exceptions import APIException
from backend.api.v1.authentication import requires_auth


class CartCheckout(Resource):
    method_decorators = [requires_auth]

    # TODO: Assert auth_user == cart.user
    def post(self, cart_id, authenticated_user):
        data = CartCheckoutSchema().load(request.get_json()).data
        cart = get_or_404(Cart, Cart.id == cart_id)
        if not cart.festival:
            raise APIException(
                status_code=400,
                message="Cart needs a Festival."
            )
        now = datetime.datetime.now()
        # TODO: Abstract.
        if cart.festival.starts_on < now + datetime.timedelta(hours=1):
            raise APIException(
                status_code=400,
                message="Festival starts too soon."
            )
        if not cart.cart_products:
            raise APIException(
                status_code=400,
                message="Cart needs some products."
            )
        with db.session.no_autoflush:
            order = Order.from_cart(cart)
            order.shipping_address = data['shipping_address']
            cart.cart_products = []
            cart.festival = None
            db.session.add(cart)
            db.session.add(order)
        db.session.flush()
        invoice = Invoice.from_order(order)
        db.session.add(invoice)
        db.session.commit()
        host_url = (
            request.environ['HTTP_ORIGIN']
            if 'HTTP_ORIGIN' in request.environ.keys() else None
        )
        order_url = (
            '{host_url}/account/orders/{order_id}/invoice'
            .format(host_url=host_url, order_id=order.id)
        )
        try:
            send_templated_email(
                cart.user.email_address,
                'FestEasy Order Confirmation - Thank You!',
                'order-confirmation.html',
                dict(
                    first_name=cart.user.first_name,
                    order_id=order.id,
                    order_url=order_url,
                ),
            )
        except:
            pass
        return OrderSchema().dump(order).data
