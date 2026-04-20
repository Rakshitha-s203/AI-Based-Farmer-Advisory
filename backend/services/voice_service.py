from gtts import gTTS
import os
import uuid

# Folder to store audio files
AUDIO_DIR = "backend/audio"

# Create folder if not exists
os.makedirs(AUDIO_DIR, exist_ok=True)


def generate_voice(text: str, lang: str = "en") -> str:
    """
    Convert text to speech and save as mp3
    Returns file path
    """

    try:
        # Unique filename
        filename = f"{uuid.uuid4()}.mp3"
        file_path = os.path.join(AUDIO_DIR, filename)

        # Generate speech
        tts = gTTS(text=text, lang=lang)
        tts.save(file_path)

        return file_path

    except Exception as e:
        print("Voice generation error:", e)
        return None
