from marshmallow import fields

from . import EntitySchema
from .festival_schema import FestivalSchema


class OrderSchema(EntitySchema):
    festival_id = fields.Integer()
    festival = fields.Nested(FestivalSchema)
    user_id = fields.Integer()
    total_rands = fields.Float()
