import sys, os
import nose
import logging
from flask import current_app
from flask.ext.script import Manager, Command, Option
from flask.ext.script import Shell, Server
from rainbow_logging_handler import RainbowLoggingHandler
import logging


sys.path.append(os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__))
    )
)
from backend import create_app, db


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
console = RainbowLoggingHandler(sys.stderr, color_funcName=('black', True))
console_formatter = logging.Formatter("[%(asctime)s] %(name)s %(funcName)s():%(lineno)d\t%(message)s")
console.setFormatter(console_formatter)
console.setLevel(logging.INFO)
logger.addHandler(console)

manager = Manager(create_app, with_default_commands=False)
manager.add_option('-c', '--config', dest='config', default='dev', required=False)

class RunServer(Server):
    def handle(self, *args, **kwargs):
        Server.handle(self, *args, **kwargs)
manager.add_command('run-api', RunServer(use_debugger=True, use_reloader=True, host='0.0.0.0'))

class RunTests(Command):
    def run(self):
        console.setLevel(logging.ERROR)
        logger.addHandler(console)
        nose.main(argv=['--where', 'backend'])
manager.add_command('run-tests', RunTests())

class CreateAll(Command):
    def run(self):
        db.create_all()
manager.add_command('create-all', CreateAll())

class DropAll(Command):
    def run(self):
        db.drop_all()
manager.add_command('drop-all', DropAll())

def _make_context():
    context = dict()
    return context

manager.add_command('shell', Shell(make_context=_make_context, use_ipython=True))

if __name__ == '__main__':
    manager.run()
