from flask import Blueprint, request, jsonify, session
from app.database import Meal, db
from app.views.auth import login_required
from app.llm import get_meal_data
from datetime import datetime
from sqlalchemy import select

bp: Blueprint = Blueprint("meals", __name__)


@bp.post("/meals")
@login_required
def add_meal():
    if not request.is_json:
        return jsonify({"detail": "Request is not valid json"}), 400
    data = request.get_json()

    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"detail": "Unauthorised access"}), 401

    date_str = data.get("date")
    name = data.get("name")
    food_weight = data.get("food_weight")

    if not all([date_str, name, food_weight]):
        return jsonify({"detail": "Missing required fields"}), 400

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return jsonify({"detail": "Invalid date format"}), 400

    meal_data = get_meal_data(name=name, food_weight=food_weight)

    if not meal_data:
        return jsonify({"detail": "Failed to get meal data from llm"}), 500


    meal = Meal(
        user_id=user_id,
        date=date,
        name=name,
        food_weight=food_weight,
        calories=meal_data.get("calories"),
        protein=meal_data.get("protein"),
        carbs=meal_data.get("carbohydrates"),
        fat=meal_data.get("fat"),
    )
    db.session.add(meal)
    db.session.commit()

    return jsonify({"detail": "Meal added successfully"}), 201


@bp.get("/meals/<date_str>")
@login_required
def get_meals_by_date(date_str: str):
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"detail": "Unauthorised access"}), 401

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return jsonify({"detail": "Invalid date format"}), 400

    stmt = select(Meal).where(Meal.user_id == user_id, Meal.date == date)
    meals = db.session.execute(stmt).scalars().all()

    meals_data = [
        {
            "id": meal.id,
            "date": meal.date,
            "name": meal.name,
            "food_weight": meal.food_weight,
            "calories": meal.calories,
            "protein": meal.protein,
            "carbohydrates": meal.carbs,
            "fat": meal.fat,
        }
        for meal in meals
    ]

    return jsonify(meals_data), 200


@bp.get("/meals/<meal_id>")
@login_required
def update_meal(meal_id: int):
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"detail": "Unauthorised access"}), 401

    # Preventing user from accessing meals of other users
    stmt = select(Meal).where(Meal.user_id == user_id, Meal.id == meal_id)
    meal = db.session.execute(stmt).scalar_one_or_none()

    if not meal:
        return jsonify({"detail": "Meal not found"}), 404

    if not request.is_json:
        return jsonify({"detail": "Request is not valid json"}), 400

    data = request.get_json()

    # TODO add additional validation for data fields
    if "name" in data:
        meal.name = data["name"]
    if "food_weight" in data:
        meal.food_weight = data["food_weight"]
    if "calories" in data:
        meal.calories = data["calories"]
    if "protein" in data:
        meal.protein = data["protein"]
    if "carbohydrates" in data:
        meal.carbs = data["carbohydrates"]
    if "fat" in data:
        meal.fat = data["fat"]

    db.session.add(meal)
    db.session.commit()

    return jsonify({"detail": "Meal updated successfully"}), 200
