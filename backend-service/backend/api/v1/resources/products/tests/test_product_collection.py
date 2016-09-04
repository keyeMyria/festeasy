from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import Product


endpoint = 'v1.productcollection'


class TestProductCollection(APITestCase):
    def test_get(self):
        product = factories.ProductFactory()
        db.session.add(product)
        db.session.commit()
        repsonse = self.api_request(
            'get',
            url_for(endpoint),
        )
        self.assertEqual(repsonse.status_code, 200, repsonse.json)
        self.assertEqual(repsonse.json['data'][0]['id'], product.id, repsonse.json)

    def test_post(self):
        product_name = 'asdf'
        data = dict(
            name=product_name,
            description='This awesome new product is awesome',
            price_rands=2,
        )
        repsonse = self.api_request(
            'post',
            url_for(endpoint),
            data=data,
        )
        self.assertEqual(repsonse.status_code, 200, repsonse.json)
        fetched_product = Product.query.first()
        self.assertIsNotNone(fetched_product, repsonse.json)
        self.assertEqual(fetched_product.name, product_name, repsonse.json)
