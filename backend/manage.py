import sys, os

from flask import current_app
from flask.ext.script import Manager, Command, Option
from flask.ext.script import Shell, Server

sys.path.append(os.path.dirname(
	os.path.dirname(
		os.path.abspath(__file__))
	)
)

from backend import create_app


manager = Manager(create_app, with_default_commands=False)
manager.add_option('-c', '--env', dest='env', default='dev', required=False)

class RunServer(Server):
    def handle(self, *args, **kwargs):
        Server.handle(self, *args, **kwargs)

manager.add_command('run-api', RunServer(use_debugger=True, use_reloader=True, host='0.0.0.0'))

def _make_context():
    context = dict()
    return context

manager.add_command('shell', Shell(make_context=_make_context, use_ipython=True))


if __name__ == '__main__':
	manager.run()