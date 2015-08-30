from flask import url_for

from backend import db
from backend.testing import APITestCase


class TestOrderProductSingleton(APITestCase):
    def test_get(self):
        order_product = self.create_order_product(
            unit_price_rands=10,
            quantity=3,
            order=self.create_order(
                event=self.create_event(name='as'),
                user=self.create_user(normal_user=True, with_cart=True),
            ),
            product=self.create_product(create_valid_product=True),
        )
        db.session.add(order_product)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for('v1.orderproductsingleton',
                    order_product_id=order_product.id
            ),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], order_product.id)
