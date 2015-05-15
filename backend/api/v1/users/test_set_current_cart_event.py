import json
from flask import url_for

from backend import db
from backend.models import User, Product
from backend.utils import APITestCase


class TestSetUserCurrentCartEvent(APITestCase):
    def test_set_current_cart_event_sets_current_cart_event(self):
        """ Test that v1.set_current_cart_event sets a users
        current_cart_event.
        """
        user = self.create_user(create_valid_session=True)
        event = self.create_event(name='test_event')
        db.session.add(event)
        db.session.add(user)
        db.session.commit()

        self.assertEqual(User.query.one().current_cart_event, None)

        response = self.api_request('post',
            url_for('v1.set_current_cart_event', user_id=user.id),
            as_user=user,
            with_session=user.sessions[0],
            data=dict(event_id=event.id)
        )

        self.assertEqual(User.query.one().current_cart_event, event)
        self.assertEqual(response.status_code, 201)

    def test_set_current_cart_event_404s_with_invalid_event_id(self):
        """ Test that v1.set_current_cart_event 404s when an invalid  
        event_id is used.
        """
        user = self.create_user(create_valid_session=True)
        event = self.create_event(name='test_event')
        db.session.add(event)
        db.session.add(user)
        db.session.commit()

        invalid_event_id = event.id + 1

        self.assertEqual(User.query.one().current_cart_event, None)

        response = self.api_request('post',
            url_for('v1.set_current_cart_event', user_id=user.id),
            as_user=user,
            with_session=user.sessions[0],
            data=dict(event_id=invalid_event_id)
        )

        self.assertEqual(response.status_code, 404)
