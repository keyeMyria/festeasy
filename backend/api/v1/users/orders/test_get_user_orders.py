import json
from flask import url_for

from backend import db
from backend.models import User, Product
from backend.testing import APITestCase


class TestGetUserOrders(APITestCase):
    def test_get_user_orders_returns_user_orders(self):
        """ Test that v1.get_user_orders returns a users
        orders.
        """
        user = self.create_user(normal_user=True, valid_session=True, with_cart=True)
        user.cart.products = [self.create_product(create_valid_product=True)]
        db.session.add(user)
        db.session.commit()

        response = self.api_request('get',
            url_for('v1.get_user_orders', user_id=user.id),
            as_user=user,
            with_session=user.sessions[0],
        )
        self.assertIsNotNone(response.json['orders'])
