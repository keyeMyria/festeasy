from marshmallow import fields

from . import EntitySchema


class ForgotPasswordTokenSchema(EntitySchema):
    user_id = fields.Integer()
    token = fields.String()
    is_valid = fields.Boolean()
    email_address = fields.String()
