from marshmallow import fields

from .base_schema import BaseSchema


class ChangePasswordSchema(BaseSchema):
    current_password = fields.String()
    new_password = fields.String()
