from flask import request
from flask_restful import Resource
from sqlalchemy import or_

from backend import db
from backend.models import Product, Category, ProductCategory
from backend.api.v1.schemas import ProductSchema


product_schema = ProductSchema()


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
        category = request.args.get('category')
        if category:
            q = filter_categories(q, category)
        search_term = request.args.get('search')
        if search_term:
            q = search(q, search_term)
        q = q.order_by(Product.created_on.desc())
        return product_schema.dump(q.all(), many=True).data

    def post(self):
        load_data = product_schema.load(request.get_json()).data
        product = Product(**load_data)
        db.session.add(product)
        db.session.commit()
        return product_schema.dump(product).data
