from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.orderproductsingleton'


class TestOrderProductSingleton(APITestCase):
    def test_get(self):
        order_product = factories.OrderProductFactory()
        db.session.add(order_product)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint,
                    order_product_id=order_product.id
                    ),
        )
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.json['id'], order_product.id, response.data)
