from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, BigInteger, String, DateTime, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import Optional
import datetime
import uvicorn

DATABASE_URL = "postgresql://user:password@localhost/dbname"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class ChatTab(Base):
    __tablename__ = "chat_tab"
    
    tab_id = Column(BigInteger, primary_key=True, index=True)
    id2 = Column(BigInteger, index=True)
    name = Column(String)
    cur_time = Column(DateTime)

class Chatting(Base):
    __tablename__ = "chatting"
    
    chat_id = Column(BigInteger, primary_key=True, index=True)
    tab_id = Column(BigInteger, ForeignKey('chat_tab.tab_id'))
    question = Column(String)
    answer = Column(String)
    timestamp = Column(DateTime)

Base.metadata.create_all(bind=engine)

app = FastAPI()

class ChatRequest(BaseModel):
    tab_id: int
    question: str

class ChatResponse(BaseModel):
    answer: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def langchain_responder(question: str) -> str:
    
    return "This is a response to your question: " + question

@app.post("/chat/", response_model=ChatResponse)
def chat(request: ChatRequest, db: SessionLocal = next(get_db())):
    # 챗봇 응답 생성
    answer = langchain_responder(request.question)
    
    # 새 채팅 기록 생성 및 데이터베이스에 저장
    new_chat = Chatting(
        tab_id=request.tab_id,
        question=request.question,
        answer=answer,
        timestamp=datetime.datetime.now()
    )
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    
    return {"answer": answer}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
