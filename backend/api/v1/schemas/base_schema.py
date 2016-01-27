from marshmallow import Schema, pre_load

from backend.exceptions import APIException


class BaseSchema(Schema):

    @pre_load
    def ensure_dict(self, data):
        return data or {}

    class Meta:
        strict = True

    def handle_error(self, error, data):
        raise APIException(
            message='Something went wrong.',
            payload=dict(
                errors=error.messages,
                data=data,
            ),
        )
