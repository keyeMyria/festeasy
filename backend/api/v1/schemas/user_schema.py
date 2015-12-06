from marshmallow import fields

from backend.api.utils import EntitySchema


class UserSchema(EntitySchema):
    first_name = fields.String()
    last_name = fields.String()
    email_address = fields.Email(dump_only=True)
    is_admin = fields.Boolean(dump_only=True)
    cart_id = fields.Integer(dump_only=True)
    password = fields.String(dump_only=True)

    class Meta:
        strict = True
