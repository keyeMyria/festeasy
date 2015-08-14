import logging
from flask import make_response, jsonify
from werkzeug.exceptions import NotFound


logger = logging.getLogger(__name__)

def get_or_404(model, ident, message="No such entity found."):
    result = model.query.filter(model.id == ident).first()
    if result is None:
        logger.warn("Model {model} with ID {id} not found.".format(model=model, id=ident))
        raise NotFound(message, response=make_response(jsonify(message=message), 404))
    return result
