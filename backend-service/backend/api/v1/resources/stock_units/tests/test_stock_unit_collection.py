from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import StockUnit


endpoint = 'v1.stockunitcollection'


class TestStockUnitCollection(APITestCase):
    def test_get(self):
        stock_unit = factories.StockUnitFactory()
        db.session.add(stock_unit)
        db.session.commit()
        repsonse = self.api_request(
            'get',
            url_for(endpoint),
        )
        self.assertEqual(repsonse.status_code, 200, repsonse.json)
        self.assertEqual(
            repsonse.json[0]['id'],
            stock_unit.id,
            repsonse.json,
        )

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
        fetched_stock_unit = StockUnit.query.first()
        self.assertIsNotNone(fetched_stock_unit, repsonse.json)
        self.assertEqual(
            fetched_stock_unit.product_id,
            product.id,
            repsonse.json,
        )
