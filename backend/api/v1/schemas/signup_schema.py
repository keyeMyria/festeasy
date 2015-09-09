from marshmallow import fields, Schema


class SignupSchema(Schema):
    email_address = fields.Email(load_only=True, required=True)
    password = fields.String(load_only=True, required=True)
    first_name = fields.String(load_only=True, required=True)

    class Meta:
        strict = True
