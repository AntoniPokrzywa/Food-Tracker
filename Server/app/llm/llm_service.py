import os
import requests
import json
from dotenv import load_dotenv
import re
import logging

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# print(GEMINI_API_KEY)
def load_prompt_template(query):
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'nutrition_prompt.txt')
    with open(template_path, 'r') as f:
        prompt_template = f.read()
    
    return prompt_template.format(query=query)

def mock_nutrition_data(food_name, weight):
    """Mock nutrition data for development when API key is not available"""
    # Common nutrition values per 100g
    nutrition_db = {
        "chicken": {"calories": 165, "protein": 31, "carbs": 0, "fats": 3.6},
        "rice": {"calories": 111, "protein": 2.6, "carbs": 23, "fats": 0.9},
        "salmon": {"calories": 208, "protein": 25, "carbs": 0, "fats": 12},
        "broccoli": {"calories": 34, "protein": 2.8, "carbs": 7, "fats": 0.4},
        "sweet potato": {"calories": 86, "protein": 1.6, "carbs": 20, "fats": 0.1},
        "banana": {"calories": 89, "protein": 1.1, "carbs": 23, "fats": 0.3},
        "apple": {"calories": 52, "protein": 0.3, "carbs": 14, "fats": 0.2},
        "beef": {"calories": 250, "protein": 26, "carbs": 0, "fats": 15},
        "pasta": {"calories": 131, "protein": 5, "carbs": 25, "fats": 1.1},
        "bread": {"calories": 265, "protein": 9, "carbs": 49, "fats": 3.2},
    }
    
    # Find the best match
    food_lower = food_name.lower()
    best_match = None
    
    for key in nutrition_db:
        if key in food_lower:
            best_match = nutrition_db[key]
            break
    
    if not best_match:
        # Default values for unknown foods
        best_match = {"calories": 100, "protein": 5, "carbs": 15, "fats": 2}
    
    # Calculate based on weight
    weight_factor = weight / 100
    print(best_match["fats"])
    print(best_match["protein"]
    )
    return {
        "calories": round(best_match["calories"] * weight_factor),
        "protein": round(best_match["protein"] * weight_factor, 1),
        "carbs": round(best_match["carbs"] * weight_factor, 1),
        "fats": round(best_match["fats"] * weight_factor, 1)
    }

def call_gemini_api(query):
    if not GEMINI_API_KEY:
        print("⚠️  No Gemini API key found. Using mock nutrition data.")
        return mock_nutrition_data("chicken", 100)
    
    prompt = load_prompt_template(query)

    url = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent" 
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, params=params, json=data, timeout=10)
        response.raise_for_status()
        result = response.json()
        logging.debug("Full API response: %s", result)
        
        text = result["candidates"][0]["content"]["parts"][0]["text"]
        logging.debug("Response text: %s", text)
        
        text = re.sub(r'```json\n|```', '', text).strip()
        logging.debug("Cleaned text: %s", text)

        json_data = json.loads(text) if text.strip().startswith("{") else {}
        logging.debug("Parsed JSON: %s", json_data)
        print(json_data)
        return json_data
    except requests.exceptions.HTTPError as e:
        logging.error("HTTP error: %s", str(e))
        return {"error": "API request failed", "details": str(e)}
    except Exception as e:
        logging.error("Parsing error: %s", str(e))
        return {"error": "Failed to parse Gemini response", "details": str(e)}