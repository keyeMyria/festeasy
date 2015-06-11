from wtforms import Form, StringField
from wtforms.validators import Required, Email


class CreateUserInvoiceForm(Form):
    """ Used to create an invoice for a user.
    """
    order_id = StringField('order_id', [Required()])
