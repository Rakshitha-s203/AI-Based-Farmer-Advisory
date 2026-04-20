from fastapi import FastAPI
from backend.routes import auth_router, chatbot_router, disease_router, weather_router, voice_router
from backend.database import Base, engine
from backend.routes.admin import router as admin_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.get("/")
def home():
    return {"message": "AgriGuard Backend Running Successfully 🌿"}


app.include_router(auth_router)
app.include_router(chatbot_router)
app.include_router(disease_router)
app.include_router(weather_router)
app.include_router(voice_router)

app.include_router(admin_router)



