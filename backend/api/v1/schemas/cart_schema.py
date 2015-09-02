from marshmallow import fields

from backend.api.utils import EntitySchema


class CartSchema(EntitySchema):
    event_id = fields.Integer()
    total_rands = fields.Float()

    class Meta:
        strict = True
