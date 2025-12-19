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
 
