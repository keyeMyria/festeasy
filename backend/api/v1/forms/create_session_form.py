from wtforms import Form, StringField
from wtforms.validators import Required, Email


class CreateSessionForm(Form):
    email_address = StringField('email_address', [Required(), Email()])
    password = StringField('password', [Required()])
