import datetime

from backend import db
from backend.models import Session, User, Product
from backend.models import UserProductCart
from backend.utils import ModelTestCase


class TestUserProductCart(ModelTestCase):
    def test_user_product_cart_creation(self):
        """ Test that a UserProductCart can be created.
        """
        user = self.create_user()
        product = self.create_product(name='abc', price_cents=99)

        cart_product = UserProductCart()
        cart_product.user = user
        cart_product.product = product

        db.session.add(cart_product)
        db.session.commit()

        fetched_cart_product = UserProductCart.query.one()

        self.assertEqual(fetched_cart_product, cart_product)
        self.assertEqual(fetched_cart_product.user, user)
        self.assertEqual(fetched_cart_product.product, product)

    def test_user_product_cart_deletion(self):
        """ Test that a UserProductCart deletion does not delete
        the user nor product.
        """
        user = self.create_user()
        product = self.create_product(name='abc', price_cents=99)

        cart_product = UserProductCart()
        cart_product.user = user
        cart_product.product = product

        db.session.add(cart_product)
        db.session.commit()

        fetched_cart_product = UserProductCart.query.one()

        self.assertEqual(fetched_cart_product, cart_product)
        self.assertEqual(fetched_cart_product.user, user)
        self.assertEqual(fetched_cart_product.product, product)

        db.session.delete(fetched_cart_product)

        self.assertEqual(UserProductCart.query.all(), list())
        self.assertEqual(User.query.one(), user)
        self.assertEqual(Product.query.one(), product)
