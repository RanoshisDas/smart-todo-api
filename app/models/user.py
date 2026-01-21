from beanie import Document
from pydantic import EmailStr
from typing import Optional
from datetime import datetime

class User(Document):
    email: EmailStr
    username: str
    hashed_password: str
    is_active: bool = True
    created_at: datetime = datetime.utcnow()
    
    class Settings:
        name = "users"
        indexes = ["email"]