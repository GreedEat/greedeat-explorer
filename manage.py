from flask_assets import ManageAssets
from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand

from werkzeug.contrib.fixers import ProxyFix

from app import Base, create_app, db_session, engine, assets


app_ = create_app()
app_.wsgi_app = ProxyFix(app_.wsgi_app)

manager = Manager(app_)
migrate = Migrate(app_, Base)

server = Server(host="0.0.0.0")


def make_shell_context():
    return dict(app=app_, db=db_session)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)
manager.add_command("runserver", server)
manager.add_command("assets", ManageAssets(assets))


@manager.command
def initdb():
   Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    manager.run()