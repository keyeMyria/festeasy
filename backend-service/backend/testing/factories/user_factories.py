from factory import Factory, SubFactory

from backend.models import User
from . import CartFactory


class UserFactory(Factory):
    class Meta:
        model = User

    first_name = 'John'
    last_name = 'Doe'
    email_address = 'johndoe@gmail.com'
    guest_token = None
    is_admin = False
    password = '123'
    cart = SubFactory(CartFactory)
