from flask import request
from flask_restful import Resource
from sqlalchemy import or_
from webargs import fields
from webargs.flaskparser import parser
from math import ceil

from backend import db
from backend.models import Product, Category, ProductCategory
from backend.api.v1.schemas import ProductSchema


product_schema = ProductSchema()
query_args = {
    'page_size': fields.Integer(
        load_from='page-size',
        missing=20,
    ),
    'page_number': fields.Integer(
        load_from='page-number',
        missing=1,
    ),
    'category': fields.String(
        missing=None,
    ),
    'search': fields.String(
        missing=None,
    ),
    'order_by': fields.String(
        load_from='order-by',
        missing=None,
    ),
    'order_direction': fields.String(
        load_from='order-direction',
        missing='desc',
    )
}


def filter_categories(q, category):
    q = q.join(ProductCategory)
    q = q.join(Category)
    q = q.filter(Category.name == category)
    return q


def search(q, search_term):
    q = q.filter(
        or_(
            Product.name.ilike("%{0}%".format(search_term)),
            Product.description.ilike("%{0}%".format(search_term)),
        )
    )
    return q


class ProductCollection(Resource):
    def get(self):
        q = Product.query
        params = parser.parse(query_args, request)
        page_size = params['page_size']
        page_number = params['page_number']
        order_by = params['order_by']
        order_direction = params['order_direction']
        if params['category']:
            q = filter_categories(q, params['category'])
        if params['search']:
            q = search(q, params['search'])
        if order_by:
            q = q.order_by(
                getattr(getattr(Product, order_by), order_direction)()
            )
        paginated_q = q.offset(page_size * (page_number - 1)).limit(page_size)
        total_count = q.count()
        return {
            'data': product_schema.dump(paginated_q.all(), many=True).data,
            'meta': {
                'total_count': total_count,
                'total_pages': ceil(total_count / page_size),
            }
        }

    def post(self):
        load_data = product_schema.load(request.get_json()).data
        product = Product(**load_data)
        db.session.add(product)
        db.session.commit()
        return product_schema.dump(product).data
