# genai.py
# import os
# from dotenv import load_dotenv
# import google as genai

# load_dotenv()

# GENAI_API_KEY = os.getenv("GENAI_API_KEY")

# if not GENAI_API_KEY:
#     raise ValueError("GENAI_API_KEY not found in environment variables")

# genai.configure(api_key=GENAI_API_KEY)

# FASHION_SYSTEM_PROMPT = """
# You are a professional fashion stylist and image consultant.

# Your tasks:
# 1. Analyze clothing items provided by the user.
# 2. Identify styling mistakes (color clash, poor fit, imbalance).
# 3. Suggest improved outfit combinations.
# 4. Be concise, practical, and modern.
# """

# def generate_outfit_suggestion(wardrobe_description: str) -> str:
#     """
#     Takes wardrobe description/tags and returns outfit suggestion text.
#     """

#     model = genai.GenerativeModel("gemini-pro")

#     response = model.generate_content(
#         FASHION_SYSTEM_PROMPT + "\n\nUser wardrobe:\n" + wardrobe_description
#     )

#     return response.text
# genai.py
import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("GENAI_API_KEY missing")

genai.configure(api_key=API_KEY)

def generate_outfit_cards(wardrobe_text: str) -> list:
    prompt = f"""
    You are a professional fashion stylist.

    Based on the wardrobe below:
    {wardrobe_text}

    Return EXACT JSON.
    Do not explain anything.
    Return a list of 3 objects.
    Each object must contain:
    title, top, bottom, shoes, note
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    try:
        return json.loads(response.text)
    except Exception as e:
        print("JSON parse failed:", e)
        return []

