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

    def test_patch(self):
        user = self.create_user(normal_user=True, with_cart=True)
        festival = self.create_festival(
            pre_populate=True,
            base_festival=self.create_base_festival(),
        )
        db.session.add(festival)
        db.session.add(user)
        db.session.commit()
        response = self.api_request(
            'patch',
            url_for(endpoint, user_id=user.id),
            data=dict(festival_id=festival.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user.cart.festival_id, festival.id)
