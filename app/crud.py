from app.database import SessionLocal
from sqlalchemy.orm import Session

from app import models, schemas

# def get_greeting(db: Session, skip: int = 0, limit: int = 1):
def get_greeting(db: Session, greeting_id: int):
    # return db.query(models.Greeting).offset(skip).limit(limit).all()
    return db.query(models.Greeting).filter(models.Greeting.id == greeting_id).first()


def get_greeting_by_message(db: Session, message: str):
    return db.query(models.Greeting).filter(models.Greeting.message == message).first()


def get_greetings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Greeting).offset(skip).limit(limit).all()


def create_greeting(db: Session, greeting: schemas.GreetingCreate):
    greeting = models.Greeting(message=greeting.message)
    db.add(greeting)
    db.commit()
    db.refresh(greeting)
    return greeting