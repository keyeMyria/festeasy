import json
from flask import url_for

from backend import db
from backend.models import User, Product
from backend.utils import APITestCase


class TestGetUser(APITestCase):
    def test_get_user_returns_user(self):
        """ Test that v1.get_user returns a user
        from the db.
        """
        user = self.create_user(create_valid_session=True)
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)

        response = self.api_request('get',
            url_for('v1.get_user', user_id=user.id),
            as_user=user,
            with_session=user.sessions[0],
        )
        self.assertEqual(response.json['user']['id'], user.id)

        # Test that correct attribs are returned:
        self.assertIsNone(response.json['user']['current_cart_event'])

    def test_get_user_404(self):
        """ Test that v1.get_user 404s for an invalid user id.
        """
        user = self.create_user(create_valid_session=True)
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)

        invalid_user_id = user.id + 1
        
        response = self.api_request(
            'get',
            url_for('v1.get_user', user_id=invalid_user_id),
            as_user=user,
            with_session=user.sessions[0],
        )
        self.assertEqual(response.status_code, 404)
