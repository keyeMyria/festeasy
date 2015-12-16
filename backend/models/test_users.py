from backend import db
from backend.models import User
from backend.testing import ModelTestCase
from backend.testing import factories


class TestUser(ModelTestCase):
    def test_user_is_not_guest(self):
        """
        Test that user.is_guest is False if a user
        has an email_address, first_name and password set.
        """
        #user = self.create_user(email_address='asd@asd.com', with_cart=True)
        user = factories.UserFactory()
        user.guest_token = None
        user.set_password('123')
        db.session.add(user)
        db.session.commit()
        fetched_user = User.query.first()
        self.assertFalse(fetched_user.is_guest)

    def test_user_is_not_guest_with_email(self):
        """
        Test that user.is_guest is False if a user
        has an email_address, first_name, password and guest_token set.
        """
        user = factories.UserFactory()
        user.email_address = 'asd@asd.com'
        user.first_name = 'Asd'
        user.set_password('asd')
        user.guest_token = 'jasduqwejj'
        db.session.add(user)
        db.session.commit()
        fetched_user = User.query.first()
        self.assertFalse(fetched_user.is_guest)

    def test_user_is_guest(self):
        """
        Test that user.is_guest is True if a user
        has only a guest_token set.
        """
        user = factories.UserFactory(
            email_address=None,
            first_name=None,
            guest_token='jasduqwejj'
        )
        db.session.add(user)
        db.session.commit()
        fetched_user = User.query.first()
        self.assertTrue(fetched_user.is_guest)

    # TODO: What is this for?
    def test_user_check_constraint_as_guest(self):
        """
        Test CheckConstraint for a guest user.
        """
        user = factories.UserFactory(
            guest_token='asd',
        )
        db.session.add(user)
        db.session.commit()
        fetched_user = User.query.first()
        self.assertIsNotNone(fetched_user)

    # TODO: What is this for?
    def test_user_check_constraint_non_guest(self):
        """
        Test CheckConstraint for a normal user.
        """
        user = self.create_user(with_cart=True)
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        self.assertEqual(User.query.first(), None)
        user.email_address = 'asd'
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        self.assertEqual(User.query.first(), None)
        user.first_name = 'asd'
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        self.assertEqual(User.query.first(), None)
        user.set_password('asd')
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        self.assertEqual(User.query.first(), user)
