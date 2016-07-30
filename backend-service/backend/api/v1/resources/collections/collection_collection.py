from flask import request
from flask_restful import Resource

from backend import db
from backend.models import Collection
from backend.api.v1.schemas import CollectionSchema


collection_schema = CollectionSchema()


class CollectionCollection(Resource):
    def get(self):
        q = Collection.query
        return collection_schema.dump(q.all(), many=True).data

    def post(self):
        load_data = collection_schema.load(request.get_json()).data
        collection = Collection(**load_data)
        db.session.add(collection)
        db.session.commit()
        return collection_schema.dump(collection).data
