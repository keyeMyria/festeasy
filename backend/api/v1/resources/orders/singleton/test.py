from flask import url_for

from backend import db
from backend.testing import APITestCase


endpoint = 'v1.ordersingleton'


class TestOrderSingleton(APITestCase):
    def test_get(self):
        order = self.create_order(
            event=self.create_event(name='asd'),
            user=self.create_user(normal_user=True, with_cart=True),
        )
        db.session.add(order)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint, order_id=order.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], order.id)
