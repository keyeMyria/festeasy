from . import BaseEmailer


class DummyEmailer(BaseEmailer):
    """
    Emailer which does nothing.
    """
    def send_email(self, to, from_name, from_address, subject, body):
        pass
