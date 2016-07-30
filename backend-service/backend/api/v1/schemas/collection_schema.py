from marshmallow import fields

from . import EntitySchema


class CollectionSchema(EntitySchema):
    order_id = fields.Integer()
