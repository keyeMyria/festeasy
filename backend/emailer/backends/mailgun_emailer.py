import requests
from flask import current_app

from . import BaseEmailer


class MailgunEmailer(BaseEmailer):
    """
    Emailer which sends emails by POSTING to mailgun's api.
    """
    def send_email(self, to, from_name, from_address, subject, body):
        response = requests.post(
            'https://api.mailgun.net/v3/{domain}/messages'.format(
                domain=current_app.config['MAILGUN_DOMAIN'],
            ),
            auth=('api', current_app.config['MAILGUN_API_KEY']),
            data={
                'to': to,
                'from': '{from_name}<{from_address}>'.format(
                    from_name=from_name,
                    from_address=from_address,
                ),
                'subject': subject,
                'html': body,
            },
        )

        if response.status_code != 200:
            raise Exception(response.text)
