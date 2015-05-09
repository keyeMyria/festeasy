from wtforms import Form, StringField, FieldList
from wtforms.validators import Required, Email


class DeleteUserCartProductForm(Form):
    user_cart_product_ids = FieldList(StringField('user_cart_product_id', [Required()]))
