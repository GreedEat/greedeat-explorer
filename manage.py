from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand

from werkzeug.contrib.fixers import ProxyFix

from app import Base, create_app, db_session, engine


app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)

manager = Manager(app)
migrate = Migrate(app, Base)

server = Server(host="0.0.0.0")


def make_shell_context():
    return dict(app=app, db=db_session)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)
manager.add_command("runserver", server)


@manager.command
def initdb():
   Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    manager.run()