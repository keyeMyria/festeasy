from flask_restful import Resource
from flask import request

from backend import db
from backend.models import Festival
from backend.api.utils import get_or_404
from backend.api.v1.schemas import FestivalSchema


class FestivalSingleton(Resource):
    def __init__(self):
        self.festival_schema = FestivalSchema()

    def get(self, festival_id):
        festival = get_or_404(Festival, Festival.id == festival_id)
        data, errors = self.festival_schema.dump(festival)
        return data

    def patch(self, festival_id):
        festival = get_or_404(Festival, Festival.id == festival_id)
        load_data, load_errors = self.festival_schema.load(request.get_json())
        for arg in load_data:
            setattr(festival, arg, load_data[arg])
        db.session.add(festival)
        db.session.commit()
        data, errors = self.festival_schema.dump(festival)
        return data
