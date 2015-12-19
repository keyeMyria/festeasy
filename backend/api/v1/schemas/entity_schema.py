from marshmallow import Schema, fields

from backend.api.v1.exceptions import APIException


class EntitySchema(Schema):
    id = fields.Integer(dump_only=True)
    created_on = fields.DateTime(dump_only=True)
    last_updated_on = fields.DateTime(dump_only=True)

    def handle_error(self, error, data):
        raise APIException(
            message='Something went wrong.',
            payload=dict(
                errors=error.messages,
                data=data,
            ),
        )
