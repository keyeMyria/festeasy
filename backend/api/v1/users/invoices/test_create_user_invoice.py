import json
from flask import url_for

from backend import db
from backend.models import User, Cart, Product
from backend.models import Order
from backend.testing import APITestCase
from backend.api.v1.users.orders.create_user_order import _create_user_order


class TestCreateUserInvoice(APITestCase):
    def test_create_user_invoice_creates_invoice(self):
        user = self.create_user(normal_user=True, valid_session=True, with_cart=True)
        product = self.create_product(create_valid_product=True)
        user.cart.products.append(product)
        event = self.create_event(name='asd')
        user.cart.event = event
        order = self.create_order()
        order.from_cart(user.cart)

        db.session.add(user)
        db.session.add(order)
        db.session.commit()

        response = self.api_request(
            'post',
            url_for('v1.create_user_invoice', user_id=user.id), 
            as_user=user,
            data=dict(order_id=order.id),
            with_session=user.sessions[0],
        )
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json['invoices']), 1)
        self.assertEqual(response.json['invoices'][0]['id'], 1)

    def test_create_user_invoice_404s(self):
        user = self.create_user(normal_user=True, valid_session=True, with_cart=True)
        product = self.create_product(create_valid_product=True)
        user.cart.products.append(product)
        event = self.create_event(name='asd')
        user.cart.event = event
        order = self.create_order()
        order.from_cart(user.cart)

        db.session.add(user)
        db.session.add(order)
        db.session.commit()

        invalid_order_id = order.id + 1

        response = self.api_request(
            'post',
            url_for('v1.create_user_invoice', user_id=user.id), 
            as_user=user,
            data=dict(order_id=invalid_order_id),
            with_session=user.sessions[0],
        )
        
        self.assertEqual(response.status_code, 404)
