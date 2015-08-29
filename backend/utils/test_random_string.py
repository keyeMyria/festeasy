from backend.testing import BackendTestCase
from backend.utils import random_string


class TestRandomString(BackendTestCase):
	def test_random_string(self):
		a = random_string(25)