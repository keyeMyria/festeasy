from wtforms import Form, StringField
from wtforms.validators import Required, Email


class CreateUserForm(Form):
    """ Used to create a new user.
    """
    email_address = StringField('email_address')
    password = StringField('password')
    first_name = StringField('first_name')
    guest_token = StringField('guest_token')
