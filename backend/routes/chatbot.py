from fastapi import APIRouter
from backend.services.gemini_service import chatbot_response
from backend.database.db import SessionLocal
from backend.database.models import Chat,Feedback,Escalation

router = APIRouter()

@router.post("/chat")
def chat(q: str, user: str):
    answer = chatbot_response(q)

    db = SessionLocal()
    chat = Chat(user=user, question=q, answer=answer)
    db.add(chat)
    db.commit()

    return {"answer": answer}


#FEEDBACK
@router.post("/feedback")
def give_feedback(user: str, message: str, rating: int):
    db = SessionLocal()
    fb = Feedback(user=user, message=message, rating=rating)
    db.add(fb)
    db.commit()
    return {"msg": "Feedback saved"}


# ESCALATION
@router.post("/escalate")
def raise_issue(user: str, issue: str):
    db = SessionLocal()
    esc = Escalation(user=user, issue=issue)
    db.add(esc)
    db.commit()
    return {"msg": "Issue submitted"}


# ADMIN CHAT LOGS
@router.get("/admin/chats")
def get_chats():
    db = SessionLocal()

    chats = db.query(Chat).all()

    return [
        {
            "user": c.user,
            "question": c.question,
            "answer": c.answer
        }
        for c in chats
    ]
