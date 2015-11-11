from flask import url_for

from backend.testing import APITestCase
from backend import db

endpoint = 'v1.cartproductcollection'


class TestCartProductCollection(APITestCase):
    def test_get(self):
        cart_product = self.create_cart_product(
            product=self.create_product(create_valid_product=True),
            cart=self.create_cart(),
        )
        db.session.add(cart_product)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[0]['id'], cart_product.id)
