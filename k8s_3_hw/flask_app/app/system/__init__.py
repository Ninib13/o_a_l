from flask import Blueprint

bp = Blueprint("system", __name__, url_prefix="/")

from .routes import *