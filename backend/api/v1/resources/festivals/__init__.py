from backend.api.v1 import v1_api
from .festivals_singleton import FestivalSingleton
from .festivals_collection import FestivalCollection


v1_api.add_resource(FestivalSingleton,
                    '/festivals/<int:festival_id>')
v1_api.add_resource(FestivalCollection,
                    '/festivals')
