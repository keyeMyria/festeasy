from wtforms import Form, FormField, FieldList
from wtforms.validators import Required, Email

from .create_user_cart_product_form import CreateUserCartProductForm


class CreateUserCartProductsForm(Form):
    """ Used to create multiple user_cart_products.
    """
    product_ids = FieldList(FormField(CreateUserCartProductForm), min_entries=1)
