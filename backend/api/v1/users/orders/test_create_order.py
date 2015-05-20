import json
from flask import url_for

from backend import db
from backend.models import User, UserCartProduct, Product
from backend.models import Order
from backend.utils import APITestCase


class TestCreateOrder(APITestCase):
    def test_create_order_creates_order_for_user(self):
        """ Test that v1.create_order creates a user_product_cart in the db.
        """
        user = self.create_user(create_valid_session=True)
        event = self.create_event(name='asd')
        product = self.create_product(name='abc', price_cents=99)

        user.cart_products.append(product)
        user.current_cart_event = event
        db.session.add(user)
        db.session.commit()

        response = self.api_request(
            'post',
            url_for('v1.create_order', user_id=user.id), 
            as_user=user,
            with_session=user.sessions[0],
        )
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json['orders']), 1)
        self.assertEqual(response.json['orders'][0]['id'], 1)

        fetched_user = User.query.one()
        fetched_order = Order.query.one()

        self.assertEqual(fetched_user.orders, [fetched_order])
        self.assertEqual(fetched_order.event, user.current_cart_event)
        self.assertEqual(fetched_order.products, [product])
