from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.ordersingleton'


class TestOrderSingleton(APITestCase):
    def setUp(self):
        super().setUp()
        self.session = factories.SessionFactory()
        db.session.add(self.session)
        db.session.commit()

    def test_get(self):
        order = factories.OrderFactory(user=self.session.user)
        db.session.add(order)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint, order_id=order.id),
            session_token=self.session.token,
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(response.json['id'], order.id, response.json)
