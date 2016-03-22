from backend.api.v1 import v1_api
from .collection_collection import CollectionCollection


v1_api.add_resource(CollectionCollection,
                    '/collections')
