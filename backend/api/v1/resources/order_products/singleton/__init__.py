from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse

from backend import db
from backend.models import OrderProduct
from backend.api.utils import get_or_404


singleton_fields = {
    'id': fields.Integer,
}

class OrderProductSingleton(Resource):
    @marshal_with(singleton_fields)
    def get(self, order_product_id):
        order_product = get_or_404(OrderProduct, OrderProduct.id == order_product_id)
        return order_product
