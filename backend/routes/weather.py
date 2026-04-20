from fastapi import APIRouter
import requests
from config import WEATHER_API_KEY

router = APIRouter()

@router.get("/weather")
def get_weather(city: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Bangalore&appid=c438d121d258701a46d0819ea5ee9e42&units=metric"
    data = requests.get(url).json()

    return {
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["main"]
    }
