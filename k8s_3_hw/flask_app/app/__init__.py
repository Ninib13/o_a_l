from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config, configureLogging

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
logger = app.logger
configureLogging()

from app import user, system, ui

app.register_blueprint(user.bp)
app.register_blueprint(system.bp)
app.register_blueprint(ui.bp)