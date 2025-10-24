import os
from flask import Flask
from bookish.models import db, migrate
from bookish.controllers import register_controllers
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)

    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 's3cr3t_k3y')

    db.init_app(app)
    migrate.init_app(app, db)

    JWTManager(app)
    register_controllers(app)

    if __name__ == "__main__":
        app.run()

    return app
