from backend.testing import GeneralTestCase
from backend.utils import random_string


class TestRandomString(GeneralTestCase):
	def test_random_string(self):
		a = random_string(25)
