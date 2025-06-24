from flask import Blueprint

bp: Blueprint = Blueprint("auth", __name__)

@bp.get("/")
def hello_world():
    return "Hello"