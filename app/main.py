from fastapi import FastAPI
from app.models import Base
from app.database import engine

app = FastAPI()


Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "FastAPI is working!"}
