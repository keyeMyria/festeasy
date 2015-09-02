from marshmallow import fields

from backend.api.utils import EntitySchema


class EventSchema(EntitySchema):
    name = fields.String()
    starts_on = fields.DateTime()
    ends_on = fields.DateTime()

    class Meta:
        strict = True
