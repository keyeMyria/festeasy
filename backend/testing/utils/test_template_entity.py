from backend.testing import BackendTestCase
from backend.testing.utils import template_entity


class TestTemplateEntity(BackendTestCase):
	def test_template_entity(self):
		template_name = 'Jason'
		template_email_address = 't@q.io'
		template_dict = {
			'name': template_name,
			'email_address': template_email_address,
		}
		kwargs_name = 'Shaun'
		kwargs_dict = {
			'name': kwargs_name,
		}
		result = template_entity(template_dict, kwargs_dict)
		self.assertEqual(result['name'], kwargs_name)
		self.assertEqual(result['email_address'], template_email_address)
