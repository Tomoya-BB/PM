from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()


def create_app(database_path=None):
    app = Flask(__name__)
    if not database_path:
        database_path = os.environ.get("APP_DATABASE_PATH", "pm.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        from . import models, views
        db.create_all()
        app.register_blueprint(views.bp)
    return app
