from flask import url_for

from backend import db
from backend.models import Session
from backend.testing import APITestCase, factories

endpoint = 'v1.signin'


class TestSignin(APITestCase):
    def test_post(self):
        email_address = 'asd@asdf.com'
        password = '123'
        first_name = 'Juan'
        user = factories.UserFactory(
            email_address=email_address,
            password=password,
            first_name=first_name,
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

        self.assertEqual(response.status_code, 202, response.json)
        self.assertEqual(response.json['user_id'], user.id, response.json)
        fetched_session = Session.query.first()
        self.assertEqual(fetched_session.user, user, response.json)
