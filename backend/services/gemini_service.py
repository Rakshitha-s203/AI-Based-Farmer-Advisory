import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-flash-lite-latest")

def chatbot_response(text):
    response = model.generate_content(text)
    return response.text

def detect_disease(image):
    prompt = "Identify plant disease and give prevention tips"
    response = model.generate_content([prompt, image])
    return response.text
