import os
basedir = os.path.split(os.path.abspath(os.path.dirname(__file__)))

class Config(object):
    SECRET_KEY = os.environ.get('APP_KEY', 'omg, it\'s a secret key!')
    DEBUG = os.environ.get('APP_DEBUG', False)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # DB_CONNECTION=mysql
    # DB_HOST=127.0.0.1
    # DB_PORT=3306
    # DB_DATABASE=laravel
    # DB_USERNAME=root
    # DB_PASSWORD=