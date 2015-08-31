from flask import url_for

from backend import db
from backend.testing import APITestCase


class TestSessionSingleton(APITestCase):
    def test_get(self):
        session = self.create_session(
            valid_session=True,
            user=self.create_user(normal_user=True, with_cart=True),
        )
        db.session.add(session)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for('v1.sessionsingleton', session_id=session.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], session.id)
