import json
from flask import url_for

from backend import db
from backend.models import User
from backend.testing import APITestCase


class TestGetProducts(APITestCase):
    def test_get_products_returns_products(self):
        """ Test that v1.get_products returns a user
        from the db.
        """
        product = self.create_product(create_valid_product=True)
        db.session.add(product)
        db.session.commit()

        response = self.api_request('get',
            url_for('v1.get_products'),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['products'][0]['id'], product.id)
