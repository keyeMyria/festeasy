from marshmallow import fields

from . import EntitySchema


class PayUSetTransactionSchema(EntitySchema):
    merchant_reference = fields.Integer(attribute='merchantReference', required=True)
    payu_reference = fields.Integer(attribute='payUReference', required=True)
    successful = fields.Boolean()
    result_message = fields.String(attribute='resultMessage')
    result_code = fields.Integer(attribute='resultCode')
    display_message = fields.String(attribute='displayMessage')
    point_of_failure = fields.String(attribute='pointOfFailure')
