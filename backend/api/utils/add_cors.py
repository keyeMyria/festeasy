import logging
from flask import request


logger = logging.getLogger(__name__)

def add_cors(response):
    logger.warn("Adding cors headers.")
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
