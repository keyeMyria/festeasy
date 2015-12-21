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
            Product.name.like("%{0}%".format(search_term)),
            Product.description.like("%{0}%".format(search_term)),
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
        products = q.all()
        return product_schema.dump(products, many=True).data

    def post(self):
        load_data = product_schema.load(request.get_json()).data
        product = Product()
        for key, val in load_data.items():
            setattr(product, key, val)
        db.session.add(product)
        db.session.commit()
        return product_schema.dump(product).data
