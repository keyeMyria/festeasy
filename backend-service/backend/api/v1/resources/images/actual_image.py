from flask import make_response, request
from flask_restful import Resource
from PIL import Image as PIL_IMAGE
from io import BytesIO
from webargs import fields
from webargs.flaskparser import parser

from backend.models import Image
from backend.api.utils import get_or_404


IMAGE_TYPE_MAP = {
    'jpg': 'jpeg',
    'jpeg': 'jpeg',
    'png': 'png',
}
query_args = {
    'height': fields.Integer(
        missing=None,
    ),
    'width': fields.Integer(
        missing=None,
    )
}


class ActualImage(Resource):
    def get(self, image_id):
        image = get_or_404(Image, Image.id == image_id)
        pil_image = PIL_IMAGE.open(BytesIO(image.file_data))
        params = parser.parse(query_args, request)
        height, width = params['height'], params['width']
        if width or height:
            pil_image.thumbnail((height or width, width or height))
        result = BytesIO()
        pil_image.save(
            result,
            IMAGE_TYPE_MAP[image.filetype.lower()],
        )
        result.seek(0)
        response = make_response(result.read())
        response.headers['Content-Type'] = 'image/{0}'.format(image.filetype)
        return response
