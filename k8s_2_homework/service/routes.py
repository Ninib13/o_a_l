# -*- coding: utf-8 -*-
from service import app
from flask import jsonify
import os

@app.route('/')
def index():
    return 'Превед медвед!\r\nНа связи: ' + os.environ['HOSTNAME'] + '\r\n'

@app.route('/health/')
def health():
    return jsonify(status='OK')