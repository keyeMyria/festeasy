from marshmallow import fields

from backend.api.utils import EntitySchema


class PaymentSchema(EntitySchema):
    amount_rands = fields.Float()

    class Meta:
        strict = True
