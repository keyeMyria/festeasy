from marshmallow import fields

from backend.api.utils import EntitySchema


class CartSchema(EntitySchema):
    festival_id = fields.Integer()
    total_rands = fields.Float()

    class Meta:
        strict = True
