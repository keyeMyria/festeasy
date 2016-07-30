from marshmallow import fields

from . import EntitySchema


class PayUTransactionSchema(EntitySchema):
    merchant_reference = fields.Integer()
    payu_reference = fields.Integer()
    successful = fields.Boolean()
    result_message = fields.String()
    result_code = fields.Integer()
    display_message = fields.String()
    point_of_failure = fields.String()
