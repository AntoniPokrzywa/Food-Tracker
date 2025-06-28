from flask import Blueprint, request, jsonify
from .llm.llm_service import call_gemini_api

bp = Blueprint('views', __name__)

@bp.route('/api/llm_parse', methods=['GET'])
def parse_food():
    query = request.args.get("query", "")
    if not query:
        return jsonify({"error": "Missing 'query' parameter in URL"}), 400

    result = call_gemini_api(query)
    return jsonify(result)