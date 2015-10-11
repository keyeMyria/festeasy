from flask import url_for

from backend import db
from backend.testing import APITestCase
from backend.models import Cart


endpoint = 'v1.usercartsingleton'


class TestUserCartSingleton(APITestCase):
    def test_get(self):
        user = self.create_user(normal_user=True)
        cart = Cart()
        user.cart = cart
        db.session.add(user)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint, user_id=user.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], user.id)