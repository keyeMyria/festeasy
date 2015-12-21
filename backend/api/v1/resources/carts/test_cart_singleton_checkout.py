import datetime
from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import Order


endpoint = 'v1.cartsingletoncheckout'


class TestCartSingletonCheckout(APITestCase):
    def test_post(self):
        the_future = datetime.datetime.now() + datetime.timedelta(days=10)
        user = factories.UserFactory()
        festival = factories.FestivalFactory(
            starts_on=the_future,
        )
        product = factories.ProductFactory(
            product_prices=[
                factories.ProductPriceFactory(amount_rands=10),
            ],
        )
        user.cart.products.append(product)
        user.cart.festival = festival
        db.session.add(user)
        db.session.commit()
        response = self.api_request(
            'post',
            url_for(endpoint, cart_id=user.cart.id)
        )
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(user.cart.products, [], response.data)
        self.assertEqual(len(user.orders), 1, response.data)
        fetched_order = Order.query.first()
        self.assertEqual(len(fetched_order.invoices), 1, response.data)
