import datetime

from backend import db
from backend.models import Event, User
from backend.models import Cart, Payment
from backend.utils import ModelTestCase


class TestPayment(ModelTestCase):
    def test_create_payment(self):
        """ Test that a Payment can be created.
        """
        product_price = 100
        user = self.create_user()
        product = self.create_product(name='abc', price_rands=product_price)
        event = self.create_event(name='asd')
        user.cart.products.append(product)
        user.cart.event = event
        order = self.create_order()
        order.from_cart(user.cart)
        invoice = self.create_invoice()
        invoice.from_order(order)

        db.session.add(invoice)
        db.session.commit()

        payment = self.create_payment(amount_rands=100, invoice=invoice)
        db.session.add(payment)
        db.session.commit()
