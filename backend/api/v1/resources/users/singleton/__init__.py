from flask_restful import Resource
from flask_restful import reqparse
from marshmallow import Schema, fields, pre_load, pre_dump
from flask import request

from backend import db
from backend.models import User
from backend.api.utils import get_or_404


class EntitySchema(Schema):
    id = fields.Integer(dump_only=True)
    created_on = fields.DateTime(dump_only=True)
    last_updated_on = fields.DateTime(dump_only=True)


class UserSchema(EntitySchema):
    email_address = fields.Email()
    first_name = fields.String()
    last_name = fields.String()
    is_admin = fields.Boolean()
    cart_id = fields.Integer()
    class Meta:
        strict = True

    @pre_load
    def pre_load(self, data):
        pass

    @pre_dump
    def pre_dump(self, data):
        del self.fields['first_name']


class UserSingleton(Resource):
    def __init__(self):
        self.user_schema = UserSchema(
            context=dict(
                authenticated_user='dummy authenticated user',
            )
        )

    def get(self, user_id):
        user = get_or_404(User, User.id == user_id)
        data, errors = self.user_schema.dump(user)
        return data

    def delete(self, user_id):
        user = get_or_404(User, User.id == user_id)
        db.session.delete(user)
        db.session.commit()
        data, errors = self.user_schema.dump(user)
        return data

    def patch(self, user_id):
        user = get_or_404(User, User.id == user_id)
        data, errors = self.user_schema.load(request.get_json())
        for arg in data:
            setattr(user, arg, data[arg])
        db.session.add(user)
        db.session.commit()
        data, errors = self.user_schema.dump(user)
        return data
