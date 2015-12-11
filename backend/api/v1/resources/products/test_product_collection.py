from flask import url_for

from backend import db
from backend.testing import APITestCase
from backend.models import Product


endpoint = 'v1.productcollection'


class TestProductCollection(APITestCase):
    def test_get(self):
        product = self.create_product(create_valid_product=True)
        db.session.add(product)
        db.session.commit()
        repsonse = self.api_request(
            'get',
            url_for(endpoint),
        )
        self.assertEqual(repsonse.status_code, 200)
        self.assertEqual(repsonse.json[0]['id'], product.id)

    def test_post(self):
        product_name = 'asdf'
        data = dict(
            name=product_name,
            description='This awesome new product is awesome',
        )
        repsonse = self.api_request(
            'post',
            url_for(endpoint),
            data=data,
        )
        self.assertEqual(repsonse.status_code, 200)
        fetched_product = Product.query.first()
        self.assertIsNotNone(fetched_product)
        self.assertEqual(fetched_product.name, product_name)
