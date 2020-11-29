import logging
from flask.logging import default_handler
from flask import has_request_context, request
from logging.config import dictConfig
import os
basedir = os.path.split(os.path.abspath(os.path.dirname(__file__)))


class Config(object):
    SECRET_KEY = os.environ.get('APP_KEY', 'omg, it\'s a secret key!')
    DEBUG = os.environ.get('APP_DEBUG', False)
    if os.environ.get('DATABASE_URL', False):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    elif os.environ.get('DB_HOST', False):
        connectionStringTemplate = "mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
        SQLALCHEMY_DATABASE_URI = connectionStringTemplate.format(DB_USERNAME=os.environ.get('DB_USERNAME'), DB_PASSWORD=os.environ.get(
            'DB_PASSWORD'), DB_HOST=os.environ.get('DB_HOST'), DB_PORT=os.environ.get('DB_PORT'), DB_DATABASE=os.environ.get('DB_DATABASE'))
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
            os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SOME_ENV_VAR=os.environ.get('SOME_ENV_VAR', '%not_set%')

    # DB_CONNECTION=mysql
    # DB_HOST=127.0.0.1
    # DB_PORT=3306
    # DB_DATABASE=laravel
    # DB_USERNAME=root
    # DB_PASSWORD=


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] [%(process)s] [%(levelname)s] in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


# class RequestFormatter(logging.Formatter):
#     def format(self, record):
#         if has_request_context():
#             record.url = request.url
#             record.remote_addr = request.remote_addr
#         else:
#             record.url = None
#             record.remote_addr = None

#         return super().format(record)


def configureLogging():
    return 0
#     formatter = RequestFormatter(
#         '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
#         '%(levelname)s in %(module)s: %(message)s'
#     )
#     default_handler.setFormatter(formatter)
