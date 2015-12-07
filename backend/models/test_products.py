from backend.testing import ModelTestCase
from backend import db

from backend.models import Product


class TestProduct(ModelTestCase):
    def test_product_price_rands(self):
        product_1 = self.create_product(
            name='10',
            cost_rands=10,
            product_prices=[
                self.create_product_price(
                    amount_rands=10,
                )
            ],
        )
        product_2 = self.create_product(
            name='20',
            cost_rands=10,
            product_prices=[
                self.create_product_price(
                    amount_rands=20,
                )
            ],
        )
        product_3 = self.create_product(
            name='30',
            cost_rands=10,
            product_prices=[
                self.create_product_price(
                    amount_rands=30,
                )
            ],
        )
        db.session.add(product_1)
        db.session.add(product_2)
        db.session.add(product_3)
        db.session.commit()
        fetched_products = Product.query.all()
        for product in fetched_products:
            self.assertEqual(
                float(product.name),
                float(product.price_rands)
            )
