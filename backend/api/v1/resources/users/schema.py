from marshmallow import fields

from backend.api.utils import EntitySchema


class UserSchema(EntitySchema):
    first_name = fields.String()
    last_name = fields.String()

    class Meta:
        strict = True


class NormalUserSchema(UserSchema):
    email_address = fields.Email(dump_only=True)
    is_admin = fields.Boolean(dump_only=True)
    cart_id = fields.Integer(dump_only=True)
    password = fields.String(dump_only=True)


class AdminUserScema(UserSchema):
    email_address = fields.Email()
    is_admin = fields.Boolean()
    cart_id = fields.Integer()
    password = fields.String()


def authenticate_and_get_schema(request):
    return None, NormalUserSchema()
