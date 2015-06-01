import json
from flask import url_for

from backend import db
from backend.models import User, Product, Cart
from backend.utils import APITestCase


class TestGetCart(APITestCase):
    def test_get_cart_returns_cart(self):
        """ Test that v1.get_cart returns a user
        cart.
        """
        user = self.create_user(create_valid_session=True)
        user.cart = Cart()
        db.session.add(user)
        db.session.commit()

        response = self.api_request('get',
            url_for('v1.get_cart', user_id=user.id),
            as_user=user,
            with_session=user.sessions[0],
        )
        self.assertEqual(response.json['cart']['id'], user.cart.id)
