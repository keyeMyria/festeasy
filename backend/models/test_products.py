from backend import db
from backend.testing import factories
from backend.testing import ModelTestCase

from . import Product


class TestProduct(ModelTestCase):
    def test_product_price_rands(self):
        product_1 = factories.ProductFactory(
            name='10',
            product_prices=[
                factories.ProductPriceFactory(amount_rands=10),
            ],
        )
        product_2 = factories.ProductFactory(
            name='20',
            product_prices=[
                factories.ProductPriceFactory(amount_rands=20),
            ],
        )
        product_3 = factories.ProductFactory(
            name='30',
            product_prices=[
                factories.ProductPriceFactory(amount_rands=30),
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
