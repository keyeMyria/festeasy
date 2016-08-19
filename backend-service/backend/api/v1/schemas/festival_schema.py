from marshmallow import fields

from . import EntitySchema


class FestivalSchema(EntitySchema):
    name = fields.String()
    starts_on = fields.DateTime()
    ends_on = fields.DateTime()
    description = fields.String()
    website_link = fields.Url()
    facebook_link = fields.Url()
    ticket_link = fields.Url()
