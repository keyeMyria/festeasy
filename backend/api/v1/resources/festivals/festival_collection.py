from flask import request
from flask_restful import Resource

from backend import db
from backend.models import Festival
from backend.api.v1.schemas import FestivalSchema


class FestivalCollection(Resource):
    def __init__(self):
        self.festival_schema = FestivalSchema()

    def get(self):
        festivals = Festival.query.all()
        data, errors = self.festival_schema.dump(festivals, many=True)
        return data
