# -*- coding:utf-8 -*-
import os

from flask import Flask
from flask_assets import Bundle, Environment

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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

bundles = {
    'coffee': Bundle('coffee/*.coffee',
                     filters='coffeescript',
                     output='js/packed.js'),
    'less': Bundle('less/*.less',
                   filters='less',
                   output='css/packed.css')
}

assets = Environment(app)


def create_app():
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    assets.register(bundles)

    app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

    from .controllers import index_blueprint
    app.register_blueprint(index_blueprint)

    from .controllers import explore_blueprint
    app.register_blueprint(explore_blueprint)

    return app