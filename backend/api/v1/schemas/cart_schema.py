from marshmallow import fields

from . import EntitySchema


class CartSchema(EntitySchema):
    festival_id = fields.Integer()
    total_rands = fields.Float()
