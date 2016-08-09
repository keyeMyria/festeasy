from marshmallow import fields

from . import BaseSchema


class RecoverPasswordSchema(BaseSchema):
    email_address = fields.String()
