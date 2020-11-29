from flask import jsonify

from . import bp
from app import Config

import os

host=os.environ.get('HOSTNAME', 'unknown')

@bp.route('/')
def index():
    return 'Превед медвед!\r\nНа связи: ' + host

@bp.route('/health')
def health():
    return jsonify(status='OK')

@bp.route('/version')
def version():
    return jsonify(version=6, host=host)

@bp.route('/config')
def getConfig():
    return jsonify(some_var=Config.SOME_ENV_VAR, connection=Config.SQLALCHEMY_DATABASE_URI, debug=Config.DEBUG)