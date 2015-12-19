from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.userordersingleton'


class TestUserOrderSingleton(APITestCase):
    def test_get(self):
        user = factories.UserFactory()
        order = factories.OrderFactory(
            user=user,
        )
        db.session.add(order)
        db.session.add(user)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint, user_id=user.id, order_id=order.id),
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(response.json['id'], order.id, response.json)
