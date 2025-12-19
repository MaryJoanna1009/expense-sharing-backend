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

from app.services import get_split_strategy
from app.schemas import ExpenseCreate, ExpenseResponse
from fastapi import HTTPException

@app.post("/expenses", response_model=ExpenseResponse)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    try:
        strategy = get_split_strategy(expense.split_type)
        split_result = strategy.calculate(expense.amount, expense.splits)

        new_expense = models.Expense(
            description=expense.description,
            amount=expense.amount,
            split_type=expense.split_type,
            paid_by=expense.paid_by,
            group_id=expense.group_id
        )

        db.add(new_expense)
        db.commit()
        db.refresh(new_expense)
        return new_expense

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

