from pydantic import BaseModel

# ---------- USER SCHEMAS ----------

class UserCreate(BaseModel):
    name: str

class UserResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


# ---------- GROUP SCHEMAS ----------

class GroupCreate(BaseModel):
    name: str

class GroupResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
 
# ---------- EXPENSE SCHEMAS ----------

class SplitDetail(BaseModel):
    user_id: int
    value: float  # amount or percentage depending on split

class ExpenseCreate(BaseModel):
    description: str
    amount: float
    paid_by: int
    group_id: int
    split_type: str  # equal / exact / percentage
    splits: list[SplitDetail]

class ExpenseResponse(BaseModel):
    id: int
    description: str
    amount: float
    split_type: str

    class Config:
        orm_mode = True
