from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.sessionsingleton'


class TestSessionSingleton(APITestCase):
    def test_get(self):
        session = factories.SessionFactory()
        db.session.add(session)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint, session_id=session.id),
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(response.json['id'], session.id, response.json)
