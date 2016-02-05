from marshmallow import fields

from . import EntitySchema


class PaymentSchema(EntitySchema):
    amount_rands = fields.Float()
