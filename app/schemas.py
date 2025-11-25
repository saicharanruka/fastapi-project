from pydantic import BaseModel, EmailStr
from datetime import datetime


class Post(BaseModel):
    title: str
    content: str
    published: bool = True

class PostResponse(Post):
    id: int
    created_at: datetime
    
    # This configuration is crucial for SQLAlchemy models
    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str