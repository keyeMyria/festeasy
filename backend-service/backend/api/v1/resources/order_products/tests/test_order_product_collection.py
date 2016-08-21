from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.orderproductcollection'


class TestOrderProductCollection(APITestCase):
    def setUp(self):
        super().setUp()
        self.session = factories.SessionFactory()
        self.order_product = factories.OrderProductFactory(
            order=factories.OrderFactory(user=self.session.user)
        )
        db.session.add_all([self.session, self.order_product])
        db.session.commit()

    def test_get(self):
        response = self.api_request(
            'get',
            url_for(
                endpoint,
                order_product_id=self.order_product.id
            ),
            session_token=self.session.token,
        )
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.json[0]['id'], self.order_product.id, response.data)
