from marshmallow import fields

from . import EntitySchema


class CategorySchema(EntitySchema):
    name = fields.String()
    description = fields.String()

    class Meta:
        strict = True
