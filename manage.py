from IPython.terminal.interactiveshell import TerminalInteractiveShell
from flask import current_app
from flask.ext.script import Manager, Command
from flask.ext.script import Shell, Server

from backend import create_app, db
from backend import models
from backend.utils import get_test_data


manager = Manager(
    create_app,
    with_default_commands=False,
)

manager.add_option(
    '-c',
    '--config',
    dest='config',
    required=True,
)


class RunServer(Server):
    def handle(self, *args, **kwargs):
        Server.handle(self, *args, **kwargs)
manager.add_command(
    'run-server',
    RunServer(
        use_debugger=True,
        use_reloader=True,
        host='127.0.0.1',
    ),
)


class CreateAll(Command):
    def run(self):
        db.create_all()
manager.add_command('create-all', CreateAll())


class DropAll(Command):
    def run(self):
        db.drop_all()
manager.add_command('drop-all', DropAll())


class InitDB(Command):
    def run(self):
        db.drop_all()
        db.create_all()
        test_data = get_test_data()
        for item in test_data:
            db.session.add(item)
        db.session.commit()
manager.add_command('init-db', InitDB())


def _make_context():
    context = dict(
        db=db,
        current_app=current_app,
    )
    context.update(vars(models))
    return context
manager.add_command('shell', Shell(make_context=_make_context))

if __name__ == '__main__':
    TerminalInteractiveShell.confirm_exit.default_value = False
    manager.run()
