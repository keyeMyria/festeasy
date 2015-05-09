import json
from flask import url_for

from backend import db
from backend.models import User, Session
from backend.utils import APITestCase


class TestCreateUser(APITestCase):
    def test_create_user_creates_user(self):
        """ Test that v1.create_user creates a user and session in the db.
        """
        self.assertIsNone(User.query.first())
        email_address = 'test@festeasy.co.za'
        password = 'test_password'
        response = self.api_request(
            'post',
            url_for('v1.create_user'), 
            data=dict(
                email_address=email_address, 
                password=password,
                first_name='Jason',
            )
        )
        user = User.query.one()
        self.assertEqual(user.email_address, email_address)
        self.assertEqual(len(Session.query.all()), 1)

    def test_create_user_returns_user_and_session(self):
        """ Test that v1.create_user returns the created user and a session.
        """
        email_address = 'test@festeasy.co.za'
        password = 'test_password'
        response = self.api_request(
            'post',
            url_for('v1.create_user'), 
            data=dict(
                email_address=email_address, 
                password=password,
                first_name='Jason',
            )
        )
        self.assertEqual(response.json['user']['email_address'], email_address)
        self.assertIsNotNone(response.json['session'])


    def test_create_user_existing_email_address(self):
        """ Test that create_user does not create duplicate users.
        Test that duplicate email address returns 409.
        """
        email_address = 'test@festeasy.co.za'
        user = self.create_user(email_address=email_address)
        db.session.add(user)
        db.session.commit()

        response = self.api_request(
            'post',
            url_for('v1.create_user'), 
            data=dict(
                email_address=email_address, 
                password='test_password',
                first_name='Meh',
            )
        )
        self.assertEqual(response.status_code, 409)
        self.assertEqual(User.query.one(), user)
