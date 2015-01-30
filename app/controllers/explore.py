# -*-coding:utf-8-*-
from flask import render_template

from . import explore_blueprint


@explore_blueprint.route('/search')
def search():
    return render_template('search.html')