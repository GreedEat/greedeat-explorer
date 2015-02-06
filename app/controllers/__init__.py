from flask import Blueprint

index_blueprint = Blueprint('index', __name__)
from .index import *

explore_blueprint = Blueprint('explore', __name__)

from .explore import *