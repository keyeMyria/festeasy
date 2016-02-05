from marshmallow import fields

from .base_schema import BaseSchema


class SignupSchema(BaseSchema):
    email_address = fields.Email(load_only=True, required=True)
    password = fields.String(load_only=True, required=True)
    first_name = fields.String(load_only=True, required=True)
