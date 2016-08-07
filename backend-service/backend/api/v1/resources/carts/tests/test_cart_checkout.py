from datetime import datetime, timedelta

from backend import db
from backend.models import Order, Session, Invoice
from backend.testing import APITestCase, factories


class TestCartCheckout(APITestCase):
    def test_cart(self):
        the_future = datetime.now() + timedelta(days=10)
        user = factories.UserFactory()
        session = factories.SessionFactory(user=user)
        festival = factories.FestivalFactory(
            starts_on=the_future,
        )
        product = factories.ProductFactory(price_rands=10)
        user.cart.cart_products.append(
            factories.CartProductFactory(product=product)
        )
        user.cart.festival = festival
        db.session.add(user)
        db.session.commit()

        self.assertEqual(Session.query.one().id, session.id)
        self.assertEqual(Order.query.count(), 0)
        self.assertEqual(Invoice.query.count(), 0)

        response = self.api_request(
            'post',
            '/api/v1/carts/{cart_id}/checkout'.format(cart_id=user.cart.id),
            session_token=session.token,
        )

        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(user.cart.cart_products, [])
        self.assertEqual(user.cart.festival, None)
        fetched_order = Order.query.one()
        self.assertEqual(len(fetched_order.invoices), 1, response.data)
        self.assertEqual(response.json['id'], fetched_order.id)
