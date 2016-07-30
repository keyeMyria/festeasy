from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.ordercollection'


class TestOrderCollection(APITestCase):
    def test_get(self):
        order = factories.OrderFactory()
        db.session.add(order)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint),
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(response.json[0]['id'], order.id, response.json)
