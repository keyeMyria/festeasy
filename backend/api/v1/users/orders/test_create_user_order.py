import json
from flask import url_for

from backend import db
from backend.models import User, Cart, Product
from backend.models import Order
from backend.testing import APITestCase
from backend.api.v1.users.orders.create_user_order import _create_user_order


class TestCreateUserOrder(APITestCase):
    def test_create_user_order_creates_order_for_user(self):
        """ Test that v1.create_user_order creates an order in the db.
        """
        user = self.create_user(normal_user=True, valid_session=True)
        event = self.create_event(name='asd')
        product = self.create_product(create_valid_product=True)

        user.cart = Cart(products=[product])
        user.cart.event = event
        db.session.add(user)
        db.session.commit()

        response = self.api_request(
            'post',
            url_for('v1.create_user_order', user_id=user.id), 
            as_user=user,
            with_session=user.sessions[0],
        )
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json['orders']), 1)
        self.assertEqual(response.json['orders'][0]['id'], 1)

        fetched_user = User.query.one()
        fetched_order = Order.query.one()

        self.assertEqual(fetched_user.orders, [fetched_order])
        self.assertEqual(fetched_order.event, event)
        self.assertEqual(fetched_order.products, [product])

    def test_create_user_order_copies_prices(self):
        """ Test that _create_user_order copies the prices of 
        products froms a users cart.
        """
        user = self.create_user(normal_user=True, valid_session=True)
        event = self.create_event(name='asd')
        product = self.create_product(create_valid_product=True)

        user.cart = Cart(products=[product])
        user.cart.event = event

        db.session.add(user)
        db.session.commit()

        order = _create_user_order(user.cart)

        self.assertEqual(order.order_products[0].sub_total_rands, product.price_rands)

    def test_create_user_order_with_no_event(self):
        """ Test that v1.create_user_order fails with 400 if
        user has no current.
        """
        user = self.create_user(normal_user=True, valid_session=True)
        product = self.create_product(create_valid_product=True)

        user.cart = Cart(products=[product])

        db.session.add(user)
        db.session.commit()

        response = self.api_request(
            'post',
            url_for('v1.create_user_order', user_id=user.id), 
            as_user=user,
            with_session=user.sessions[0],
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(user.orders, list())
