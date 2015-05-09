from wtforms import Form, StringField, FieldList
from wtforms.validators import Required, Email


class CreateUserCartProductForm(Form):
    product_ids = FieldList(StringField('product_id', [Required()]))
