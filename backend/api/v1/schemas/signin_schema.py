from marshmallow import fields

from .base_schema import BaseSchema


class SigninSchema(BaseSchema):
    email_address = fields.Email(load_only=True, required=True)
    password = fields.String(load_only=True, required=True)
