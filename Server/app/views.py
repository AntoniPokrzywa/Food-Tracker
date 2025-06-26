from flask import Blueprint, request, jsonify
from .llm_service import call_gemini_api

bp = Blueprint('views', __name__)

@bp.route('/api/llm_parse', methods=['POST'])
def parse_food():
    data = request.get_json()
    query = data.get("query", "")
    result = call_gemini_api(query)
    return jsonify(result)