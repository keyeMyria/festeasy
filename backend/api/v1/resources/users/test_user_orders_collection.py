from flask import url_for

from backend import db
from backend.testing import APITestCase


endpoint = 'v1.userordercollection'


class TestUserOrderCollection(APITestCase):
    def test_get(self):
        user = self.create_user(normal_user=True, with_cart=True)
        order = self.create_order(
            festival=self.create_festival(name='asdf'),
            user=user,
        )
        db.session.add(order)
        db.session.add(user)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint, user_id=user.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[0]['id'], order.id)
