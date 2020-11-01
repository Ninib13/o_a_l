from flask import jsonify

from . import bp

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