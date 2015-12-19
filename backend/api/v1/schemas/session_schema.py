from marshmallow import fields

from . import EntitySchema
from backend.api.v1.exceptions import APIException


class SessionSchema(EntitySchema):
    token = fields.String()
    expires_on = fields.DateTime()
    user_id = fields.Integer()

    class Meta:
        strict = True

    def handle_error(self, error, data):
        raise APIException(
            message='Somthing went wrong.',
            payload={
                'data': data,
                'errors': error.messages,
            },
        )
