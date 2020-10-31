# -*- coding: utf-8 -*-
from service import app
from flask import jsonify
import os

host=os.environ.get('HOSTNAME', 'unknown')

@app.route('/')
def index():
    return 'Превед медвед!\r\nНа связи: ' + host

@app.route('/health')
def health():
    return jsonify(status='OK')

@app.route('/version')
def version():
    return jsonify(version=3, host=host)