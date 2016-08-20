from marshmallow import fields

from . import EntitySchema


class GroupSchema(EntitySchema):
    name = fields.String()
    description = fields.String()
