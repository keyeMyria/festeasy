from flask import url_for

from backend import db
from backend.models import Session
from backend.testing import APITestCase


endpoint = 'v1.signin'


class TestSignin(APITestCase):
    def test_post(self):
        email_address = 'asd@asdf.com'
        password = '123'
        first_name = 'Juan'
        user = self.create_user(
            email_address=email_address,
            password=password,
            first_name=first_name,
            with_cart=True,
        )
        db.session.add(user)
        db.session.commit()

        response = self.api_request(
            'post',
            url_for(endpoint),
            data=dict(
                email_address=email_address,
                password=password,
            )
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['user_id'], user.id)
        fetched_session = Session.query.first()
        self.assertEqual(fetched_session.user, user)
