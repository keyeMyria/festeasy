import json
from flask import url_for

from backend import db
from backend.models import User, Product
from backend.utils import APITestCase


class TestGetUserOrders(APITestCase):
    def test_get_user_orders_returns_user_orders(self):
        """ Test that v1.get_user_orders returns a users
        orders.
        """
        user = self.create_user(create_normal_user=True, create_valid_session=True)
        user.cart.products = [self.create_product(name='asd', price_rands=123)]
        db.session.add(user)
        db.session.commit()

        response = self.api_request('get',
            url_for('v1.get_user_orders', user_id=user.id),
            as_user=user,
            with_session=user.sessions[0],
        )
        self.assertIsNotNone(response.json['orders'])
