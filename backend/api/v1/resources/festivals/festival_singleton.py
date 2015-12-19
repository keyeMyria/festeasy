from flask_restful import Resource
from flask import request

from backend import db
from backend.models import Festival
from backend.api.utils import get_or_404
from backend.api.v1.schemas import FestivalSchema


festival_schema = FestivalSchema()


class FestivalSingleton(Resource):
    def get(self, festival_id):
        festival = get_or_404(Festival, Festival.id == festival_id)
        return festival_schema.dump(festival).data

    def patch(self, festival_id):
        festival = get_or_404(Festival, Festival.id == festival_id)
        load_data = festival_schema.load(request.get_json()).data
        for arg in load_data:
            setattr(festival, arg, load_data[arg])
        db.session.add(festival)
        db.session.commit()
        return festival_schema.dump(festival).data
