from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from . import user, system

    app.register_blueprint(user.bp)
    app.register_blueprint(system.bp)

    return app