from flask import url_for

from backend import db
from backend.testing import APITestCase


endpoint = 'v1.userordersingleton'


class TestUserOrderSingleton(APITestCase):
    def test_get(self):
        user = self.create_user(normal_user=True, with_cart=True)
        order = self.create_order(
            festival=self.create_festival(
                pre_populate=True,
                name='asdf',
                base_festival=self.create_base_festival(),
            ),
            user=user,
        )
        db.session.add(order)
        db.session.add(user)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint, user_id=user.id, order_id=order.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], order.id)
