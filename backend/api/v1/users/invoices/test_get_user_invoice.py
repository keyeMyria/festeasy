import json
from flask import url_for

from backend import db
from backend.models import User, Product, Invoice
from backend.utils import APITestCase


class TestGetUserInvoices(APITestCase):
    def test_get_user_invoices_returns_user_invoice(self):
        """ Test that v1.get_user_invoice returns a users
        invoices.
        """
        user = self.create_user(create_normal_user=True, create_valid_session=True)
        product = self.create_product(name='asd', price_rands=10)
        product_2 = self.create_product(name='qwe', price_rands=10)
        event = self.create_event(name='asd')
        user.cart.products.append(product)
        user.cart.products.append(product_2)
        user.cart.event = event
        
        order = self.create_order()
        order.from_cart(user.cart)

        invoice = self.create_invoice()
        invoice.from_order(order)

        db.session.add(invoice)
        db.session.add(user)
        db.session.commit()

        response = self.api_request('get',
            url_for('v1.get_user_invoice', user_id=user.id, invoice_id=invoice.id),
            as_user=user,
            with_session=user.sessions[0],
        )
        self.assertIsNotNone(response.json['invoice'])
        self.assertEqual(response.json['invoice']['id'], 1)
