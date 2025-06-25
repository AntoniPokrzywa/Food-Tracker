import os
from dotenv import load_dotenv
from flask import Flask
from app.database import db


def create_app():
    app: Flask = Flask(__name__)
    load_dotenv()

    username = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT", "5432")
    database_name = os.getenv("POSTGRES_DB")

    if not all([username, password, host, database_name]):
        raise ValueError("Database configuration is missing")

    database_uri = f"postgresql://{username}:{password}@{host}:{port}/{database_name}"

    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.views.auth import bp as auth_bp

    app.register_blueprint(auth_bp)

    return app
