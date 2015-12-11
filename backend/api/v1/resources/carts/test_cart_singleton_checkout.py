from flask import url_for

from backend import db
from backend.testing import APITestCase
from backend.models import Order


endpoint = 'v1.cartsingletoncheckout'


class TestCartSingletonCheckout(APITestCase):
    def test_post(self):
        user = self.create_user(normal_user=True, with_cart=True)
        festival = self.create_festival(
            pre_populate=True,
            base_festival=self.create_base_festival(),
        )
        product = self.create_product(create_valid_product=True)
        user.cart.products.append(product)
        user.cart.festival = festival
        db.session.add(user)
        db.session.commit()
        response = self.api_request(
            'post',
            url_for(endpoint, cart_id=user.cart.id)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user.cart.products, [])
        self.assertEqual(len(user.orders), 1)
        fetched_order = Order.query.first()
        self.assertEqual(len(fetched_order.invoices), 1)
