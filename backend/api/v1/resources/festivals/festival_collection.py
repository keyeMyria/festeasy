from flask_restful import Resource

from backend.models import Festival
from backend.api.utils import marshal_or_fail
from backend.api.v1.schemas import FestivalSchema


class FestivalCollection(Resource):
    def get(self):
        festivals = Festival.query.all()
        return marshal_or_fail('dump', festivals, FestivalSchema(), many=True)
