from sqlalchemy import Column, Integer, String
from backend.database.db import Base

# 👤 USERS
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

# 💬 CHAT LOGS
class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True)
    user = Column(String)
    question = Column(String)
    answer = Column(String)

# ⭐ FEEDBACK
class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True)
    user = Column(String)
    message = Column(String)
    rating = Column(Integer)

# ⚠️ ESCALATION
class Escalation(Base):
    __tablename__ = "escalations"
    id = Column(Integer, primary_key=True)
    user = Column(String)
    issue = Column(String)
    status = Column(String, default="Pending")
