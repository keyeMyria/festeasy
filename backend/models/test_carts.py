import datetime

from backend import db
from backend.models import Event, User
from backend.models import Cart
from backend.utils import ModelTestCase


class TestCart(ModelTestCase):
    def test_cart_total_rands(self):
        """ Test that Cart total_rands sums up 
        CartProduct sub_total_rands.
        """
        price = 10
        user = self.create_user()
        product_1 = self.create_product(name='asd', price_rands=price)
        product_2 = self.create_product(name='qwe', price_rands=price * 2)

        cart_product_1 = self.create_cart_product(cart=user.cart, product=product_1,
        	quantity=2)
        cart_product_2 = self.create_cart_product(cart=user.cart, product=product_2,
        	quantity=1)

        db.session.add(cart_product_1)
        db.session.add(cart_product_2)
        db.session.add(user)
        db.session.commit()

        fetched_cart = Cart.query.one()

        self.assertEqual(fetched_cart.total_rands, price * 4)

