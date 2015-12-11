from backend import db
from backend.models import Cart
from backend.testing import ModelTestCase


class TestCart(ModelTestCase):
    def test_cart_total_rands(self):
        """
        Test that Cart total_rands sums up
        CartProduct sub_total_rands.
        """
        price = 10
        user = self.create_user(normal_user=True, with_cart=True)
        product_1 = self.create_product(
            name='A',
            cost_rands=10,
            product_prices=[
                self.create_product_price(
                    amount_rands=price,
                )
            ],
        )
        product_2 = self.create_product(
            name='B',
            cost_rands=10,
            product_prices=[
                self.create_product_price(
                    amount_rands=price * 2,
                )
            ],
        )
        cart_product_1 = self.create_cart_product(
            cart=user.cart,
            product=product_1,
            quantity=2,
        )
        cart_product_2 = self.create_cart_product(
            cart=user.cart,
            product=product_2,
            quantity=1,
        )
        db.session.add(cart_product_1)
        db.session.add(cart_product_2)
        db.session.add(user)
        db.session.commit()
        fetched_cart = Cart.query.first()
        self.assertEqual(fetched_cart.total_rands, price * 4)
