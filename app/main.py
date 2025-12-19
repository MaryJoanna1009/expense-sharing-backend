from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app import models, schemas

app = FastAPI(title="Expense Sharing Application")

Base.metadata.create_all(bind=engine)

# ---------- ROOT ----------

@app.get("/")
def root():
    return {"message": "Expense Sharing Backend is running 🚀"}

# ---------- USER APIs ----------

@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# ---------- GROUP APIs ----------

@app.post("/groups", response_model=schemas.GroupResponse)
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    db_group = models.Group(name=group.name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

@app.get("/groups", response_model=list[schemas.GroupResponse])
def get_groups(db: Session = Depends(get_db)):
    return db.query(models.Group).all()
