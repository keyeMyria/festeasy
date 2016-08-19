from backend.api.v1 import v1_api

from .image_singleton import ImageSingleton
from .actual_image import ActualImage


v1_api.add_resource(
    ImageSingleton,
    '/images/<int:image_id>'
)
v1_api.add_resource(
    ActualImage,
    '/images/<int:image_id>/image'
)
