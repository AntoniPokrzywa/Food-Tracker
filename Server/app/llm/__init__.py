# empty file to mark this directory as a package

from .llm_service import call_gemini_api, mock_nutrition_data

def get_meal_data(name, food_weight):
    """Get nutrition data for a meal using LLM or mock data"""
    if not name or not food_weight:
        return None
    
    try:
        # Try to get data from Gemini API first
        query = f"Food: {name}, Weight: {food_weight}g"
        result = call_gemini_api(query)
        
        # If API fails or no key, use mock data
        if "error" in result or not result:
            return mock_nutrition_data(name, food_weight)
        
        return result
    except Exception as e:
        print(f"Error getting meal data: {e}")
        return mock_nutrition_data(name, food_weight)