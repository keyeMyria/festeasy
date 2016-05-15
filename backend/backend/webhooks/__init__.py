from flask import Blueprint


webhooks = Blueprint('webhooks', __name__)


@webhooks.route('/')
def hi():
    return 'Webhooks Here.'

import backend.webhooks.payu_ipn
