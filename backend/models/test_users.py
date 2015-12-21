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
        user = factories.UserFactory(
            guest_token=None,
            password='123',
        )
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
        user = factories.UserFactory(
            password='123',
            guest_token='asdf',
        )
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
            guest_token='jasduqwejj',
            password=None,
        )
        db.session.add(user)
        db.session.commit()
        fetched_user = User.query.first()
        self.assertTrue(fetched_user.is_guest)

    # TODO: Improve test.
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

    # TODO: Improve test.
    def test_user_check_constraint_non_guest(self):
        """
        Test CheckConstraint for a normal user.
        """
        user = factories.UserFactory(
            first_name=None,
            last_name=None,
            email_address=None,
            guest_token=None,
            password=None,
        )
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
