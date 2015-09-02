from marshmallow import fields

from backend.api.utils import EntitySchema


class OrderProductSchema(EntitySchema):
    event_id = fields.Integer()
    user_id = fields.Integer()
    total_rands = fields.Float()
    amount_rands = fields.Float()

    class Meta:
        strict = True
