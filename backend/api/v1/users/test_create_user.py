import json
from flask import url_for

from backend import db
from backend.models import User, Session, Cart
from backend.utils import APITestCase


class TestCreateUser(APITestCase):
    def test_create_user_creates_normal_user(self):
        """ Test that v1.create_user creates a normal user and session in the db.
        Normal user is a user with an email_address, password and first_name.
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
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['user']['email_address'], email_address)
        self.assertIsNotNone(response.json['session'])

    def test_create_user_creates_guest_user(self):
        """ Test that v1.create_user creates a guest user and session in the db.
        Guest user is a user with a guest_token and no email_address, password or first_name.
        """
        guest_token = '123'
        response = self.api_request(
            'post',
            url_for('v1.create_user'), 
            data=dict(
                guest_token=guest_token,
            )
        )
        user = User.query.one()
        self.assertEqual(len(Session.query.all()), 1)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['user']['guest_token'], guest_token)
        self.assertIsNotNone(response.json['session'])

    def test_create_user_existing_email_address_409s(self):
        """ Test that create_user does not create duplicate users.
        Test that duplicate email address returns 409.
        """
        email_address = 'test@festeasy.co.za'
        user = self.create_user(email_address=email_address, create_normal_user=True, create_valid_cart=True)
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

    def test_create_user_existing_guest_token_409s(self):
        """ Test that create_user does not create duplicate users with guest_token.
        Test that duplicate guest_token returns 409.
        """
        guest_token = 'asd'
        user = self.create_user(cart=Cart(), guest_token=guest_token)
        db.session.add(user)
        db.session.commit()

        response = self.api_request(
            'post',
            url_for('v1.create_user'), 
            data=dict(
                guest_token=guest_token,
            )
        )
        self.assertEqual(response.status_code, 409)
        self.assertEqual(User.query.one(), user)

    def test_create_user_merges_users(self):
        """ Test when a guest user signs up.
        """
        guest_token = 'asd'
        user = self.create_user(cart=Cart(), guest_token=guest_token)
        db.session.add(user)
        db.session.commit()

        email_address = 'test@festeasy.com'
        password = 'asd'
        first_name = 'qwe'

        response = self.api_request(
            'post',
            url_for('v1.create_user'), 
            data=dict(
                email_address=email_address,
                guest_token=guest_token,
                password=password,
                first_name=first_name,
            )
        )
        self.assertEqual(response.status_code, 201)
        fetched_user = User.query.one()
        self.assertEqual(fetched_user, user)
        self.assertEqual(fetched_user.email_address, email_address)
        self.assertTrue(fetched_user.has_password(password))
        self.assertEqual(fetched_user.guest_token, guest_token)
        self.assertEqual(fetched_user.first_name, first_name)
        self.assertEqual(fetched_user.cart.id, 1)
