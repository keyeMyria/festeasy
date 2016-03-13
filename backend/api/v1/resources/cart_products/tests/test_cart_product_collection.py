from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.cartproductcollection'


class TestCartProductCollection(APITestCase):
    def test_get(self):
        cart_product = factories.CartProductFactory(
            product=factories.ProductFactory(),
            cart=factories.CartFactory(),
        )
        db.session.add(cart_product)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint),
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(response.json[0]['id'], cart_product.id, response.json)
