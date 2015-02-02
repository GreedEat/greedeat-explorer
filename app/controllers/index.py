# -*-coding:utf-8-*-
from flask import render_template, send_from_directory
from . import index_blueprint
from app import app


@index_blueprint.route('/')
@index_blueprint.route('/index')
def index():
    return render_template('index.jade')


@app.route('/static/<path>')
def get_static(path):
    return send_from_directory('static', path)