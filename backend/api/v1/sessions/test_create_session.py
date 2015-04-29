import json
from flask import url_for

from backend import db
from backend.models import User, Session
from backend.utils import APITestCase


class TestCreateSession(APITestCase):
    def test_create_session_creates_session(self):
        """ Test that a session is created for a user who
        supplies a correct email address and password combination.
        """
        email_address = 'test@festeasy.co.za'
        password = 'test_password'
        user = self.create_user(password=password, email_address=email_address)
        db.session.add(user)
        db.session.commit()

        self.assertIsNone(Session.query.first())

        response = self.client.post(
            url_for('v1.create_session'), 
            data=dict(
                email_address=email_address, 
                password=password,
            )
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['user']['email_address'], email_address)
        self.assertIsNotNone(response.json['session'])
        self.assertEqual(len(Session.query.all()), 1)
        self.assertEqual(Session.query.first().user, user)

    def test_create_session_handles_incorrect_email_address(self):
        """ Test that a session is not created for a user who
        supplies an incorrect email address.
        Test that 401 is returned when an incorrect email address is 
        supplied.
        """
        email_address = 'test@festeasy.co.za'
        password = 'test_password'
        user = self.create_user(password=password, email_address=email_address)
        db.session.add(user)
        db.session.commit()

        incorrect_email_address = 'incorrect@festeasy.co.za'

        response = self.client.post(
            url_for('v1.create_session'), 
            data=dict(
                email_address=incorrect_email_address, 
                password=password,
            )
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(len(Session.query.all()), 0)

    def test_create_session_handles_incorrect_password(self):
        """ Test that a session is not created for a user who
        supplies an incorrect password.
        Test that 401 is returned when an incorrect password is 
        supplied.
        """
        email_address = 'test@festeasy.co.za'
        password = 'test_password'
        user = self.create_user(password=password, email_address=email_address)
        db.session.add(user)
        db.session.commit()

        incorrect_password = 'incorrect_password'

        response = self.client.post(
            url_for('v1.create_session'), 
            data=dict(
                email_address=email_address, 
                password=incorrect_password,
            )
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(len(Session.query.all()), 0)