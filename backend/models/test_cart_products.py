from backend import db
from backend.testing import ModelTestCase


class TestCartProduct(ModelTestCase):
    def test_cart_product_sub_total_rands(self):
        price = 10
        user = self.create_user(normal_user=True, with_cart=True)
        product = self.create_product(
            create_valid_product=True,
            price_rands=price
        )
        cart_product = self.create_cart_product(product=product, quantity=2)
        user.cart.cart_products.append(cart_product)
        db.session.add(user)
        db.session.commit()
        self.assertEqual(cart_product.sub_total_rands, price * 2)
