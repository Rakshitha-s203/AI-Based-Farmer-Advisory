from fastapi import APIRouter
from backend.services.voice_service import generate_voice

router = APIRouter(prefix="/voice", tags=["Voice"])

@router.post("/speak")
def speak(data: dict):
    text = data.get("text")
    lang = data.get("lang", "en")

    audio_path = generate_voice(text, lang)

    if audio_path:
        return {
            "status": "success",
            "audio_path": audio_path
        }
    else:
        return {
            "status": "error",
            "message": "Voice generation failed"
        }
