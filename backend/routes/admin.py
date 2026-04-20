
from fastapi import APIRouter
from backend.database.db import SessionLocal
from backend.database.models import User, Chat, Feedback, Escalation

router = APIRouter(prefix="/admin")


# FEEDBACK
@router.get("/feedback")
def get_feedback():
    db = SessionLocal()
    return db.query(Feedback).all()


# ESCALATIONS
@router.get("/escalations")
def get_escalations():
    db = SessionLocal()
    return db.query(Escalation).all()


# UPDATE ESCALATION STATUS
@router.post("/resolve")
def resolve_escalation(id: int):
    db = SessionLocal()
    esc = db.query(Escalation).filter(Escalation.id == id).first()
    esc.status = "Resolved"
    db.commit()
    return {"msg": "Updated"}
