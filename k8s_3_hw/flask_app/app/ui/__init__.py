from flask import Blueprint
bp = Blueprint("ui", __name__, url_prefix="/ui")
from .routes import *