from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def initialize():
    db = SessionLocal()
    greeting = crud.get_greeting_by_message(db, "hello world")
    if greeting is None:
        greeting = schemas.GreetingCreate
        greeting.message = "hello world"
        crud.create_greeting(db, greeting) 


@app.get("/")
async def root():
    # return {"message": "Hello World"}
    return RedirectResponse(url="/docs/")

@app.post("/greetings/", response_model=schemas.Greeting)
def create_greeting(greeting: schemas.GreetingCreate, db: Session = Depends(get_db)):
    message = crud.get_greeting_by_message(db, message=greeting.message)
    if message:
        raise HTTPException(status_code=400, detail=f"Greeting already exists: {message}")
    return crud.create_greeting(db=db, greeting=greeting)

@app.get("/greetings/", response_model=List[schemas.Greeting])
def read_greetings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    greetings = crud.get_greetings(db, skip=skip, limit=limit)
    return greetings

@app.get("/greetings/{greeting_id}", response_model=schemas.Greeting)
def read_greeting(greeting_id: int, db: Session = Depends(get_db)):
    greeting = crud.get_greeting(db, greeting_id=greeting_id)
    if greeting is None:
        raise HTTPException(status_code=404, detail="Greeting not found")
    return greeting

