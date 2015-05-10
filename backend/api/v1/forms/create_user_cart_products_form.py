from wtforms import Form, StringField, FieldList
from wtforms.validators import Required, Email


class CreateUserCartProductsForm(Form):
    product_ids = FieldList(StringField('product_id', [Required()]))
