from werkzeug.exceptions import NotFound

from backend import db
from backend.utils import APITestCase
from backend.models import User
from backend.api.utils.get_or_404 import get_or_404


class TestGetOr404(APITestCase):
    def test_get_or_404_returns_element(self):
        user = self.create_user(create_normal_user=True)
        db.session.add(user)
        db.session.commit()

        self.assertEqual(get_or_404(User, user.id), user)

    def test_get_or_404_raises_on_missing_element(self):
        with self.assertRaises(NotFound) as cm:
            get_or_404(User, 0)

        self.assertEqual(cm.exception.get_response().status_code, 404)
