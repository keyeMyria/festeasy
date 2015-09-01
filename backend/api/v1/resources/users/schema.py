from marshmallow import fields

from backend.api.utils import EntitySchema


class UserSchema(EntitySchema):
    email_address = fields.Email()
    first_name = fields.String()
    last_name = fields.String()
    is_admin = fields.Boolean()
    cart_id = fields.Integer()
    password = fields.String()

    class Meta:
        strict = True
