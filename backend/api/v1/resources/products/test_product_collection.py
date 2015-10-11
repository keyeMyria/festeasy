from flask import url_for

from backend import db
from backend.testing import APITestCase


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
