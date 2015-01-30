# -*- coding:utf-8 -*-
from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from flask_assets import Environment, Bundle

from config import config


app = Flask(__name__)

config_name = "default"
engine = create_engine(config[config_name].SQLALCHEMY_DATABASE_URI,
                       convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=False,
                                         expire_on_commit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def create_app():
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

    assets = Environment(app)
    coffee = Bundle('coffee/*.coffee',
                    filters='coffeescript',
                    output='js/packed.js')
    assets.register('coffee', coffee)

    less = Bundle('less/*.css',
                  filters='less',
                  output='css/packed.css')
    assets.register('less', less)
    assets.init_app(app)

    from .controllers import index_blueprint
    app.register_blueprint(index_blueprint)

    from .controllers import explore_blueprint
    app.register_blueprint(explore_blueprint)

    return app