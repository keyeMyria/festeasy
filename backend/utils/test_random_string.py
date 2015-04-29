from backend.utils.general_test_case import GeneralTestCase
from backend.utils import random_string


class TestRandomString(GeneralTestCase):
	def test_random_string(self):
		a = random_string(25)
