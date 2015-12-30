from flask import current_app

from . import BaseEmailer


class FileEmailer(BaseEmailer):
    """
    Emailer which writes emails to file.
    Can be used for testing.
    """
    def send_email(self, to, from_name, from_address, subject, body):
        email = dict(
            to=to,
            from_name=from_name,
            from_address=from_address,
            subject=subject,
            body=body,
        )
        with open(current_app.config['FILE_EMAILER_PATH'], 'w') as f:
            f.write(str(email))
