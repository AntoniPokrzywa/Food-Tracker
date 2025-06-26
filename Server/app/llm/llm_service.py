import os
import requests
import json
from dotenv import load_dotenv
import re
import logging

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def load_prompt_template(query):
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'nutrition_prompt.txt')
    with open(template_path, 'r') as f:
        prompt_template = f.read()
    
    return prompt_template.format(query=query)

def call_gemini_api(query):
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
        response = requests.post(url, headers=headers, params=params, json=data)
        response.raise_for_status()
        result = response.json()
        logging.debug("Pełna odpowiedź API: %s", result)
        
        text = result["candidates"][0]["content"]["parts"][0]["text"]
        logging.debug("Tekst odpowiedzi: %s", text)
        
        text = re.sub(r'```json\n|```', '', text).strip()
        logging.debug("Oczyszczony tekst: %s", text)

        json_data = json.loads(text) if text.strip().startswith("{") else {}
        logging.debug("Sparowany JSON: %s", json_data)
        
        return json_data
    except requests.exceptions.HTTPError as e:
        logging.error("Błąd HTTP: %s", str(e))
        return {"error": "API request failed", "details": str(e)}
    except Exception as e:
        logging.error("Błąd parsowania: %s", str(e))
        return {"error": "Failed to parse Gemini response", "details": str(e)}