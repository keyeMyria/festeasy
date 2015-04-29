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
                first_name='Jason',
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
                first_name='Jason',
            )
        )
        self.assertEqual(response.json['user']['email_address'], email_address)


    def test_create_user_existing_email_address(self):
        """ Test that create_user does not create duplicate users.
        Test that duplicate email address returns 409.
        """
        email_address = 'test@festeasy.co.za'
        user = self.create_user(email_address=email_address)
        db.session.add(user)
        db.session.commit()

        response = self.client.post(
            url_for('v1.create_user'), 
            data=dict(
                email_address=email_address, 
                password='test_password',
                first_name='Meh',
            )
        )
        self.assertEqual(response.status_code, 409)
        self.assertEqual(User.query.one(), user)