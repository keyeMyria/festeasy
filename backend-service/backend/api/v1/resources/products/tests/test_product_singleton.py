from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import Product


endpoint = 'v1.productsingleton'


class TestProductSingleton(APITestCase):
    def test_get(self):
        product = factories.ProductFactory()
        db.session.add(product)
        db.session.commit()
        repsonse = self.api_request(
            'get',
            url_for(endpoint, product_id=product.id),
        )
        self.assertEqual(repsonse.status_code, 200, repsonse.json)
        self.assertEqual(repsonse.json['data']['id'], product.id, repsonse.json)

    def test_patch(self):
        product = factories.ProductFactory()
        data = {
            'name': 'new_product_name',
        }
        db.session.add(product)
        db.session.commit()
        repsonse = self.api_request(
            'patch',
            url_for(endpoint, product_id=product.id),
            data=data,
        )
        self.assertEqual(repsonse.status_code, 200, repsonse.json)
        self.assertEqual(repsonse.json['data']['id'], product.id, repsonse.json)
        fetched_product = Product.query.one()
        self.assertEqual(fetched_product.name, data['name'], repsonse.json)
