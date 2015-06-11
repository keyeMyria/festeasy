import json
from flask import url_for

from backend import db
from backend.models import User, Cart, Product
from backend.models import Order
from backend.utils import APITestCase
from backend.api.v1.users.orders.create_user_order import _create_user_order


class TestCreateUserInvoice(APITestCase):
    def test_create_user_invoice_creates_invoice(self):
        user = self.create_user(create_valid_session=True)
        product = self.create_product(name='asd', price_rands=10)
        user.cart.products.append(product)
        event = self.create_event(name='asd')
        user.cart.event = event
        order = self.create_order(create_from_cart=True, user=user)

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
        #self.assertEqual(len(response.json['invoices']), 1)
        #self.assertEqual(response.json['invoices'][0]['id'], 1)
