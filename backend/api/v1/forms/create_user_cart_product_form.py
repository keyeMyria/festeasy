from wtforms import Form, StringField, FieldList
from wtforms.validators import Required, Email


class CreateUserCartProductForm(Form):
    """ Used to create a user_cart_product.
    """
    product_id = StringField('product_id', [Required()])
