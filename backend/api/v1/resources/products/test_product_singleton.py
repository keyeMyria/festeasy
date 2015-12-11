from flask import url_for

from backend import db
from backend.testing import APITestCase
from backend.models import Product


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

    def test_patch(self):
        product = self.create_product(create_valid_product=True)
        product_name = 'name_a'
        product.name = product_name
        new_product_name = 'name_b'
        data = {
            'name': new_product_name,
        }
        db.session.add(product)
        db.session.commit()
        repsonse = self.api_request(
            'patch',
            url_for(endpoint, product_id=product.id),
            data=data,
        )
        self.assertEqual(repsonse.status_code, 200)
        fetched_product = Product.query.one()
        self.assertEqual(fetched_product.name, new_product_name)
