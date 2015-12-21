from marshmallow import fields, Schema


from backend.api.v1.exceptions import APIException


class SigninSchema(Schema):
    email_address = fields.Email(load_only=True, required=True)
    password = fields.String(load_only=True, required=True)

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
