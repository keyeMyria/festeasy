from flask import request
from flask_restful import Resource

from backend import db
from backend.models import Product, ProductCategory as PC
from backend.api.utils import get_or_404
from backend.api.v1.schemas import ProductSchema


product_schema = ProductSchema()


class ProductSingleton(Resource):
    def get(self, product_id):
        product = get_or_404(Product, Product.id == product_id)
        return {
            'data': product_schema.dump(product).data,
        }

    # TODO: Test and fix hacks.
    def patch(self, product_id):
        product = get_or_404(Product, Product.id == product_id)
        load_data = product_schema.load(request.get_json()).data
        for key, val in load_data.items():
            setattr(product, key, val)
        category_ids = request.get_json().get('category-ids') if request.get_json() else None
        if category_ids is not None:
            PC.query.filter(
                PC.product_id == product_id,
                ~PC.category_id.in_(category_ids),
            ).delete(synchronize_session='fetch')
            for category_id in category_ids:
                existing_pc = (PC.query
                    .filter(
                        PC.product_id == product_id,
                        PC.category_id == category_id,
                    ).one_or_none())
                if not existing_pc:
                    db.session.add(
                        PC(product_id=product_id, category_id=category_id)
                    )
        db.session.add(product)
        db.session.commit()
        return {
            'data': product_schema.dump(product).data,
        }
