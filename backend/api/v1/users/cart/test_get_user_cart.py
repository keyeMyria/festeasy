import json
from flask import url_for

from backend import db
from backend.models import User, Product, Cart
from backend.testing import APITestCase


class TestGetCart(APITestCase):
    def test_get_user_cart_returns_cart(self):
        """ Test that v1.get_user_cart returns a user
        cart.
        """
        user = self.create_user(normal_user=True, valid_session=True)
        user.cart = Cart()
        db.session.add(user)
        db.session.commit()

        response = self.api_request('get',
            url_for('v1.get_user_cart', user_id=user.id),
            as_user=user,
            with_session=user.sessions[0],
        )
        self.assertEqual(response.json['cart']['id'], user.cart.id)
