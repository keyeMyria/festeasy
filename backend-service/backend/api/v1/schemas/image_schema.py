from marshmallow import fields

from . import EntitySchema


class ImageSchema(EntitySchema):
    filename = fields.String()
    filetype = fields.String()
