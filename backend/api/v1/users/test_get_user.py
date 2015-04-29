import json
from flask import url_for

from backend import db
from backend.models import User
from backend.utils import APITestCase


class TestGetUser(APITestCase):
    def test_get_user_returns_user(self):
        """ Test that v1.get_user returns a user
        from the db.
        """
        email_address = 'test@festeasy.co.za'
        user = User(email_address=email_address, password='test_password')
        db.session.add(user)
        db.session.commit()

        db.session.refresh(user)
        response = self.client.get(
            url_for('v1.get_user', user_id=user.id)
        )
        self.assertEqual(response.json['user']['id'], user.id)

    def test_get_user_404(self):
        """ Test that v1.get_user 404s for an invalid user id.
        """
        email_address = 'test@festeasy.co.za'
        user = User(email_address=email_address, password='test_password')
        db.session.add(user)
        db.session.commit()

        db.session.refresh(user)
        invalid_user_id = user.id + 1
        
        response = self.client.get(
            url_for('v1.get_user', user_id=invalid_user_id)
        )
        self.assertEqual(response.status_code, 404)