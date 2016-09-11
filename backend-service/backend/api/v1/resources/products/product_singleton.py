import requests
from flask import request
from flask_restful import Resource

from backend import db
from backend.models import Product, ProductCategory as PC, Image
from backend.api.utils import get_or_404
from backend.api.v1.schemas import ProductSchema
from backend.api.v1.authentication import requires_auth


product_schema = ProductSchema()


class ProductSingleton(Resource):
    def get(self, product_id):
        product = get_or_404(Product, Product.id == product_id)
        return {
            'data': product_schema.dump(product).data,
        }

    # TODO: Test and fix hacks.
    @requires_auth
    def patch(self, product_id, authenticated_user):
        assert authenticated_user.is_admin is True
        product = get_or_404(Product, Product.id == product_id)
        load_data = product_schema.load(request.get_json()).data
        for key, val in load_data.items():
            setattr(product, key, val)
        image_url = request.get_json().get('image-url') if request.get_json() else None
        image_type = request.get_json().get('image-type') if request.get_json() else None
        if image_url and image_type:
            r = requests.get(image_url)
            product.thumbnail_image = Image(file_data=r.content, filetype=image_type)
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
