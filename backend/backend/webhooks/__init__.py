from flask import Blueprint


webhooks = Blueprint('webhooks', __name__)


import backend.webhooks.payu_ipn


@webhooks.route('/')
def hi():
    return 'Webhooks Here.'
