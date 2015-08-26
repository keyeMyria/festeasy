import datetime

from backend import db
from backend.models import Session, User, Product
from backend.models import Cart, Order
from backend.models import CartProduct
from backend.testing import ModelTestCase


class TestCartProduct(ModelTestCase):
    def test_cart_product_sub_total_rands(self):
        price = 10
        user = self.create_user(create_normal_user=True)
        user.cart = Cart()
        product_1 = self.create_product(create_valid_product=True, price_rands=price)
        product_2 = self.create_product(create_valid_product=True, price_rands=price * 2)

        cart_product_1 = self.create_cart_product(product=product_1, quantity=2)
        cart_product_2 = self.create_cart_product(product=product_2, quantity=1)

        user.cart.cart_products.append(cart_product_1)
        user.cart.cart_products.append(cart_product_2)

        db.session.add(user)
        db.session.commit()

        self.assertEqual(cart_product_1.sub_total_rands, price * 2)
        self.assertEqual(cart_product_2.sub_total_rands, price * 2)
