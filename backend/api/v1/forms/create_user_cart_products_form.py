from wtforms import Form, StringField, FieldList
from wtforms.validators import Required, Email


class CreateUserCartProductsForm(Form):
    """ Used to create multiple user_cart_products.
    """
    product_ids = FieldList(StringField('product_id', [Required()]))
