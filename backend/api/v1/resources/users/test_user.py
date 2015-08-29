from flask import url_for

from backend import db
from backend.testing import APITestCase
from backend.models import User


class TestUserResource(APITestCase):
    def test_get(self):
        user = self.create_user(normal_user=True, with_cart=True)
        db.session.add(user)
        db.session.commit()
        response = self.api_request(
            'get', 
            url_for('v1.userresource', user_id=user.id),
        )
        self.assertEqual(response.json['id'], user.id)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
    	user = self.create_user(normal_user=True, with_cart=True)
    	db.session.add(user)
    	db.session.commit()
    	response = self.api_request(
    		'delete',
    		url_for('v1.userresource', user_id=user.id),
    	)
    	self.assertIsNone(User.query.first())
    	self.assertEqual(response.json['id'], user.id)
    	self.assertEqual(response.status_code, 200)

    def test_patch(self):
    	first_name = 'a'
    	new_first_name = 'b'
    	user = self.create_user(first_name=first_name, normal_user=True, with_cart=True)
    	db.session.add(user)
    	db.session.commit()
    	response = self.api_request(
    		'patch',
    		url_for('v1.userresource', user_id=user.id),
    		data=dict(
    			first_name=new_first_name,
    		)
    	)
    	fetched_user = User.query.first()
    	self.assertEqual(fetched_user.first_name, new_first_name)
    	self.assertEqual(response.json['id'], user.id)
    	self.assertEqual(response.status_code, 200)
