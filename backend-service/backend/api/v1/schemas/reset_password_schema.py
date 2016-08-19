from marshmallow import fields

from .base_schema import BaseSchema


class ResetPasswordSchema(BaseSchema):
    token = fields.String()
    password = fields.String()
