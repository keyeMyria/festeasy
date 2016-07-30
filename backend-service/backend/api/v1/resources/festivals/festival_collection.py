from flask import request
from flask_restful import Resource
from dateutil.parser import parse

from backend.models import Festival
from backend.api.v1.schemas import FestivalSchema


festival_schema = FestivalSchema()


def filter_starts_on(q):
    starts_on_min = request.args.get('starts-on-gt')
    starts_on_max = request.args.get('starts-on-lt')
    if starts_on_min:
        starts_on_min_dt = parse(starts_on_min)
        q = q.filter(Festival.starts_on >= starts_on_min_dt)
    if starts_on_max:
        starts_on_max_dt = parse(starts_on_max)
        q = q.filter(Festival.starts_on <= starts_on_max_dt)
    return q


class FestivalCollection(Resource):
    def get(self):
        q = Festival.query
        q = filter_starts_on(q)
        return festival_schema.dump(q.all(), many=True).data
