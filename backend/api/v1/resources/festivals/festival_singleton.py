from flask_restful import Resource
from flask import request

from backend import db
from backend.models import Festival
from backend.api.utils import get_or_404, marshal_or_fail
from backend.api.v1.schemas import FestivalSchema


class FestivalSingleton(Resource):
    def get(self, festival_id):
        festival = get_or_404(Festival, Festival.id == festival_id)
        return marshal_or_fail('dump', festival, FestivalSchema())

    def patch(self, festival_id):
        festival = get_or_404(Festival, Festival.id == festival_id)
        load_data = marshal_or_fail(
            'load', request.get_json(), FestivalSchema())
        for arg in load_data:
            setattr(festival, arg, load_data[arg])
        db.session.add(festival)
        db.session.commit()
        return marshal_or_fail('dump', festival, FestivalSchema())
