from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.ordercollection'


class TestOrderCollection(APITestCase):
    def setUp(self):
        super().setUp()
        self.session = factories.SessionFactory()
        db.session.add(self.session)
        db.session.commit()

    def test_get(self):
        order = factories.OrderFactory(user=self.session.user)
        db.session.add(order)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint),
            session_token=self.session.token,
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(response.json[0]['id'], order.id, response.json)
