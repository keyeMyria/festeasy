from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.ordersingleton'


class TestOrderSingleton(APITestCase):
    def test_get(self):
        order = factories.OrderFactory()
        db.session.add(order)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint, order_id=order.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], order.id)
