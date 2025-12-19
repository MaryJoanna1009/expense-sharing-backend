 
from fastapi import FastAPI
from app.database import Base, engine
from app import models

app = FastAPI(title="Expense Sharing Application")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Expense Sharing Backend is running 🚀"}
