import json
import datetime
from flask import url_for

from backend import db
from backend.models import User, Session
from backend.utils import APITestCase


class TestDeleteSession(APITestCase):
    def test_delete_session_deletes_session(self):
        """ Test that a session is deleted.
        """
        email_address = 'test@festeasy.co.za'
        password = 'test_password'
        user = User(email_address=email_address, password=password)
        expires_on = datetime.datetime.now() + datetime.timedelta(days=1)
        session = Session(token='abc', user=user, expires_on=expires_on)
        db.session.add(user)
        db.session.commit()

        self.assertEqual(Session.query.one(), session)

        response = self.client.delete(
            url_for('v1.delete_session', session_id=session.id)
        )

        self.assertEqual(response.status_code, 201)
        self.assertIsNone(Session.query.first())
   