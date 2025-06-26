import os
import requests
import json
from dotenv import load_dotenv
import re

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def call_gemini_api(query):
    prompt = f"""
You are a nutrition analysis assistant. Given a food name and its quantity in grams, return the estimated nutritional values (for the provided weight) in the following JSON format:

{{
  "name": "food name (with quantity)",
  "calories": int,            // kcal
  "protein": float,           // grams
  "fat": float,               // grams
  "carbohydrates": float      // grams
}}

Input format: "<food> <weight in grams>", e.g. "chicken breast 150g", "kebab 500g", "rice 200g". 

Only respond with the JSON object, no explanation or additional text.

Input: {query}
""".strip()


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
        print("Pełna odpowiedź API:", result)  # Logowanie pełnej odpowiedzi
        text = result["candidates"][0]["content"]["parts"][0]["text"]
        print("Tekst odpowiedzi:", text)  # Logowanie tekstu odpowiedzi
        text = re.sub(r'```json\n|```', '', text).strip()
        print("Oczyszczony tekst:", text)
        json_data = json.loads(text) if text.strip().startswith("{") else {}
        print("Sparowany JSON:", json_data)  # Logowanie wyniku parsowania
        return json_data
    except requests.exceptions.HTTPError as e:
        print("Błąd HTTP:", str(e))  # Logowanie błędów HTTP
        return {"error": "API request failed", "details": str(e)}
    except Exception as e:
        print("Błąd parsowania:", str(e))  # Logowanie błędów parsowania
        return {"error": "Failed to parse Gemini response", "details": str(e)}