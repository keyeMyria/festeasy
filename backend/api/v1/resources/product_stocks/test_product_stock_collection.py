from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import ProductStock


endpoint = 'v1.productstockcollection'


class TestProductStockCollection(APITestCase):
    def test_get(self):
        product_stock = factories.ProductStockFactory()
        db.session.add(product_stock)
        db.session.commit()
        repsonse = self.api_request(
            'get',
            url_for(endpoint),
        )
        self.assertEqual(repsonse.status_code, 200, repsonse.json)
        self.assertEqual(repsonse.json[0]['id'], product_stock.id, repsonse.json)

    def test_post(self):
        product = factories.ProductFactory()
        supplier = factories.SupplierFactory()
        db.session.add(supplier)
        db.session.add(product)
        db.session.commit()
        data = dict(
            supplier_id=supplier.id,
            product_id=product.id,
            cost_rands=10,
        )
        repsonse = self.api_request(
            'post',
            url_for(endpoint),
            data=data,
        )
        self.assertEqual(repsonse.status_code, 200, repsonse.json)
        fetched_product_stock = ProductStock.query.first()
        self.assertIsNotNone(fetched_product_stock, repsonse.json)
        self.assertEqual(fetched_product_stock.product_id, product.id, repsonse.json)
