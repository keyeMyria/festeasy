import datetime
from flask import request
from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import parser

from backend.models import Festival
from backend.api.v1.schemas import FestivalSchema


festival_schema = FestivalSchema()
query_args = {
    'checkoutable': fields.Bool(
        missing=None,
    )
}


# TODO: Test.
# TODO: Abstract.
def filter_checkoutable(q):
    now = datetime.datetime.now()
    return q.filter(Festival.starts_on > now + datetime.timedelta(hours=1))


class FestivalCollection(Resource):
    def get(self):
        params = parser.parse(query_args, request)
        checkoutable = params['checkoutable']
        q = Festival.query
        if checkoutable:
            q = filter_checkoutable(q)
        return festival_schema.dump(q.all(), many=True).data
