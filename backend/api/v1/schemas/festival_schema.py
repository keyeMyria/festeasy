from marshmallow import fields

from backend.api.utils import EntitySchema


class FestivalSchema(EntitySchema):
    name = fields.String()
    starts_on = fields.DateTime()
    ends_on = fields.DateTime()
    description = fields.String()

    class Meta:
        strict = True
