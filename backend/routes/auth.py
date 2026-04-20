from fastapi import APIRouter
from backend.database.db import SessionLocal
from backend.database.models import User

router = APIRouter(prefix="/auth")

@router.post("/register")
def register(username: str, password: str):
    db = SessionLocal()

    # check if user already exists
    existing = db.query(User).filter(User.username == username).first()
    if existing:
        return {"msg": "user already exists"}

    new_user = User(username=username, password=password)
    db.add(new_user)
    db.commit()   # ✅ VERY IMPORTANT

    return {"msg": "success"}

@router.post("/login")
def login(username: str, password: str):
    db = SessionLocal()

    user = db.query(User).filter(
        User.username == username,
        User.password == password
    ).first()

    if user:
        return {"msg": "success"}
    else:
        return {"msg": "fail"}



# GET USERS (ADMIN)
@router.get("/admin/users")
def get_users():
    db = SessionLocal()

    users = db.query(User).all()

    return [{"username": u.username} for u in users]

