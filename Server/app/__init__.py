import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from app.database import db


def create_app():
    app: Flask = Flask(__name__)
    CORS(app, supports_credentials=True, origins=["http://localhost:5173"])
    load_dotenv()

    # Use SQLite for development/testing if no PostgreSQL config
    username = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT", "5432")
    database_name = os.getenv("POSTGRES_DB")

    if all([username, password, host, database_name]):
        # Use PostgreSQL if all config is provided
        database_uri = f"postgresql://{username}:{password}@{host}:{port}/{database_name}"
    else:
        # Fallback to SQLite for development
        database_uri = "sqlite:///food_tracker.db"
        print("Using SQLite database for development")

    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")

    db.init_app(app)

    with app.app_context():
        db.create_all()
        # Add some test data if database is empty
        from app.database import User
        from sqlalchemy import select
        if db.session.execute(select(User)).first() is None:
            add_test_data()

    from app.views.auth import bp as auth_bp
    from app.views.meals import bp as meals_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(meals_bp)

    return app


def add_test_data():
    """Add test user and meals for development"""
    from app.database import User, Meal
    from werkzeug.security import generate_password_hash
    from datetime import datetime, timedelta
    
    # Create test user
    test_user = User(
        email="test@example.com",
        password=generate_password_hash("password123"),
        name="Test User"
    )
    db.session.add(test_user)
    db.session.commit()
    
    # Create some test meals
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    
    test_meals = [
        {
            "user_id": test_user.id,
            "name": "Chicken Breast",
            "food_weight": 150,
            "calories": 165,
            "protein": 31,
            "carbs": 0,
            "fat": 3.6,
            "date": today
        },
        {
            "user_id": test_user.id,
            "name": "Brown Rice",
            "food_weight": 100,
            "calories": 111,
            "protein": 2.6,
            "carbs": 23,
            "fat": 0.9,
            "date": today
        },
        {
            "user_id": test_user.id,
            "name": "Broccoli",
            "food_weight": 80,
            "calories": 27,
            "protein": 3.7,
            "carbs": 5.6,
            "fat": 0.3,
            "date": today
        },
        {
            "user_id": test_user.id,
            "name": "Salmon",
            "food_weight": 120,
            "calories": 208,
            "protein": 25,
            "carbs": 0,
            "fat": 12,
            "date": yesterday
        },
        {
            "user_id": test_user.id,
            "name": "Sweet Potato",
            "food_weight": 100,
            "calories": 86,
            "protein": 1.6,
            "carbs": 20,
            "fat": 0.1,
            "date": yesterday
        }
    ]
    
    for meal_data in test_meals:
        meal = Meal(**meal_data)
        db.session.add(meal)
    
    db.session.commit()
    print("Test data added successfully!")
    print("Test user: test@example.com / password123")
