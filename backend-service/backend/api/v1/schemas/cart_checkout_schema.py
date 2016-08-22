from marshmallow import fields

from . import BaseSchema


class CartCheckoutSchema(BaseSchema):
    shipping_address = fields.String()
