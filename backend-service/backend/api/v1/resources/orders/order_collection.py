from flask import request
from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import parser

from backend.models import Order
from backend.api.v1.schemas import OrderSchema
from backend.api.v1.authentication import requires_auth


order_schema = OrderSchema()
query_args = {
    'user_id': fields.String(
        load_from='user-id',
        missing=None,
    )
}


class OrderCollection(Resource):
    method_decorators = [requires_auth]

    def get(self, authenticated_user):
        params = parser.parse(query_args, request)
        q = Order.query
        # TODO: Test filter.
        user_id = params['user_id']
        if user_id:
            q = q.filter(Order.user_id == user_id)
        return order_schema.dump(q.all(), many=True).data
