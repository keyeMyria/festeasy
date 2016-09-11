from flask import request
from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import parser

from backend.models import Category, ProductCategory
from backend.api.v1.schemas import CategorySchema


category_schema = CategorySchema()
query_args = {
    'product_id': fields.Integer(
        load_from='product-id',
        missing=None,
    ),
}


def product_filter(q, product_id):
    q = q.join(ProductCategory)
    return q.filter(ProductCategory.product_id == product_id)


class CategoryCollection(Resource):
    def get(self):
        params = parser.parse(query_args, request)
        q = Category.query
        if params['product_id']:
            q = product_filter(q, params['product_id'])
        return {
            'data': category_schema.dump(q.all(), many=True).data,
        }
