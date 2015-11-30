from flask_restful import Resource

from backend import db
from backend.models import Cart, Order
from backend.api.utils import get_or_404


class CartSingletonCheckout(Resource):
    def post(self, cart_id):
        cart = get_or_404(Cart, Cart.id == cart_id)
        order = Order()
        order.from_cart(cart)
        cart.products = []
        cart.festival = None
        db.session.add(cart)
        db.session.add(order)
        db.session.commit()
