import pytest
from app.llm.llm_service import call_gemini_api

@pytest.mark.parametrize("food", ["lasagne 300g", "kebab 500g", "kurczak 150g", "ryż 200g"])
def test_call_gemini_api_returns_valid_macros_with_quantity(food):
    result = call_gemini_api(food)
    assert isinstance(result, dict), "Result should be a dictionary"
    
    if "error" in result:
        pytest.skip(f"API call failed: {result['details']}")

    # Validate expected keys
    for key in ["calories", "protein", "fat", "carbohydrates"]:
        assert key in result, f"Missing key '{key}' in result"
        assert isinstance(result[key], (int, float)), f"{key} should be a number"
    
    # Validate name field
    assert "name" in result, "Missing 'name' in result"
    assert isinstance(result["name"], str)
    assert result["name"].startswith(food.split()[0]), "'name' should reflect food item"