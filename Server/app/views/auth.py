from flask import Blueprint, request, jsonify, session
from app.database import db, User
from app.views.utils import login_required
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import select, exc, Select, Row

bp: Blueprint = Blueprint("auth", __name__)


@bp.post("/register")
def register():
    if not request.is_json:
        return jsonify({"Request is not valid json"}), 400
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    if db.session.execute(select(User).where(User.email == email)).scalar() is not None:
        return jsonify({"error": "Account with this email already exists"}), 400

    password_hash: str = generate_password_hash(password=password)
    user: User = User(email=email, password=password_hash)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Account created successfully"}), 201


@bp.post("/login")
def login():
    if not request.is_json:
        return jsonify({"Request is not valid json"}), 400

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    try:
        user: User = db.session.execute(
            select(User).where(User.email == email)
        ).scalar_one()
    except exc.NoResultFound:
        return jsonify({"error": "Invalid credentials"}), 400
    except exc.MultipleResultsFound:
        return jsonify({"error": "Internal Server Error"}), 500

    if not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 400

    session["user_id"] = user.id
    return jsonify({"message": "Login successful"}), 200


@bp.post("/logout")
def logout():
    session["user_id"] = None
    return jsonify({"message": "Logout successful"}), 200


# temporary route for testing
@bp.get("/user")
@login_required
def get_user():
    user: User = db.session.execute(
        select(User).where(User.id == session["user_id"])
    ).scalar_one()
    return jsonify({"email": user.email}), 200
