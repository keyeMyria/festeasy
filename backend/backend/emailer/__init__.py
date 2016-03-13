from werkzeug import import_string


class Emailer(object):
    def __init__(self, app=None):
        self.app = app
        if self.app is not None:
            self.init_app(app)

    def init_app(self, app):
        backend = import_string('backend.emailer.backends.{0}'.format(
            app.config['EMAILER_BACKEND'],
        ))
        self.backend = backend()

    def send_email(self, *args, **kwargs):
        return self.backend.send_email(*args, **kwargs)
