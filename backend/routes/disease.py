from fastapi import APIRouter, UploadFile, File
import google.generativeai as genai
from PIL import Image
import io

router = APIRouter(prefix="/disease")

# 🔑 ADD YOUR GEMINI API KEY
genai.configure(api_key="AIzaSyCkdQ9wMGkiW6jsXLKqtv1Odmqha3z1Ypo")

model = genai.GenerativeModel("gemini-flash-lite-latest")  # ✅ updated model

@router.post("/detect")
async def detect(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))

        prompt = """
        Analyze this plant leaf image and answer:
        1. What disease is this?
        2. Give simple prevention tips (farmer-friendly)
        3. Keep answer short and clear
        """

        response = model.generate_content([prompt, image])

        return {
            "result": response.text
        }

    except Exception as e:
        return {"result": f"Error: {str(e)}"}
