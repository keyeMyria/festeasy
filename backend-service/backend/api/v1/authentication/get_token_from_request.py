import logging
from webargs import fields
from webargs.flaskparser import parser


logger = logging.getLogger(__name__)


# TODO: Test.
def get_token_from_request():
    """Returns an authentication token from the Authorization header, or
    the 'auth-token' query parameter.
    """
    args = {
        'header_token': fields.String(
            location='headers',
            load_from='Authorization',
            missing='',
        ),
        'query_token': fields.String(
            location='query',
            load_from='auth-token',
            missing='',
        )
    }
    token = None
    params = parser.parse(args)
    header_token = params['header_token']
    query_token = params['query_token']
    if header_token:
        logger.debug('Loading token from Authorization header.')
        token = header_token
    elif query_token:
        logger.debug('Loading auth token from query parameter.')
        token = query_token
    else:
        logger.debug('No token in request header or query parameter.')
    return token
