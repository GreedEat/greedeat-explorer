# -*-coding:utf-8-*-
from flask import render_template

from . import index_blueprint


@index_blueprint.route('/')
@index_blueprint.route('/index')
def index():
    return render_template('index.html')