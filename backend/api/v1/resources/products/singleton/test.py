from flask import url_for

from backend import db
from backend.testing import APITestCase


endpoint = 'v1.productsingleton'


class TestProductSingleton(APITestCase):
    def test_get(self):
        product = self.create_product(create_valid_product=True)
        db.session.add(product)
        db.session.commit()
        repsonse = self.api_request(
            'get',
            url_for(endpoint, product_id=product.id),
        )
        self.assertEqual(repsonse.status_code, 200)
        self.assertEqual(repsonse.json['id'], product.id)
