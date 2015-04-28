import json
from flask import url_for

from backend import db
from backend.models import User
from backend.utils import APITestCase


class TestCreateUser(APITestCase):
    def test_create_user_creates_user(self):
        """ Test that v1.create_user creates a user
        in the db.
        """
        self.assertIsNone(User.query.first())
        email_address = 'test@festeasy.co.za'
        password = 'test_password'
        response = self.client.post(
            url_for('v1.create_user'), 
            data=dict(
                email_address=email_address, 
                password=password,
            )
        )
        user = User.query.one()
        self.assertEqual(user.email_address, email_address)

    def test_create_user_returns_user(self):
        """ Test that v1.create_user returns the created
        user.
        """
        email_address = 'test@festeasy.co.za'
        password = 'test_password'
        response = self.client.post(
            url_for('v1.create_user'), 
            data=dict(
                email_address=email_address, 
                password=password,
            )
        )
        self.assertEqual(response.json['user']['email_address'], email_address)
