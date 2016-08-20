from flask import request
from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import parser

from backend.models import Category
from backend.api.v1.schemas import CategorySchema


category_schema = CategorySchema()
args = {
    'name': fields.String(
        load_from='name',
    )
}


class CategoryCollection(Resource):
    def get(self):
        params = parser.parse(args, request)
        name = params['name']
        q = Category.query
        if name is not None:
            q = q.filter(Category.name == name)
        return category_schema.dump(q.all(), many=True).data
