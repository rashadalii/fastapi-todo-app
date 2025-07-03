from pydantic import BaseModel, Field, validator
from typing import Optional, List
from enum import Enum



class UserCreate(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    username: str
    password: str = Field(..., min_length=6)

    @validator("password")
    def password_length(cls, value):
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters long.")
        return value

class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]
    username: str

    class Config:
        orm_mode = True



class TaskStatus(str, Enum):
    new = "New"
    in_progress = "In Progress"
    completed = "Completed"

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.new

    

class TaskUpdate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPair(Token):
    refresh_token: str

class RefreshTokenRequest(BaseModel):
    refresh_token: str