from backend import db
from backend.testing import ModelTestCase
from backend.testing import factories


class TestCartProduct(ModelTestCase):
    def test_cart_product_sub_total_rands(self):
        price = 10
        user = factories.UserFactory()
        product = factories.ProductFactory(
            product_prices=[
                factories.ProductPriceFactory(amount_rands=price),
            ],
        )
        cart_product = factories.CartProductFactory(
            product=product,
            quantity=2,
        )
        user.cart.cart_products.append(cart_product)
        db.session.add(user)
        db.session.commit()
        self.assertEqual(cart_product.sub_total_rands, price * 2)
