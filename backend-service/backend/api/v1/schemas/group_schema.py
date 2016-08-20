from marshmallow import fields

from . import EntitySchema
from . import CategorySchema


class GroupSchema(EntitySchema):
    name = fields.String()
    description = fields.String()
    categories = fields.Nested(CategorySchema(), many=True)
