import json
import datetime
from flask import url_for

from backend import db
from backend.models import User, Session
from backend.testing import APITestCase


class TestDeleteSession(APITestCase):
    def test_delete_session_deletes_session(self):
        """ Test that a session is deleted.
        """
        user = self.create_user(normal_user=True, valid_session=True, with_cart=True)
        session = user.sessions[0]
        db.session.add(user)
        db.session.commit()

        self.assertEqual(Session.query.one(), session)

        response = self.api_request(
            'delete',
            url_for('v1.delete_session', session_id=session.id),
            as_user=user,
            with_session=session,
        )

        self.assertEqual(response.status_code, 201)
        self.assertIsNone(Session.query.first())
   