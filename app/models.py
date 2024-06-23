from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(..., min_length=2, max_length=30)
    username: str = Field(..., min_length=2, max_length=20)
    email: str
    hashed_password: str


class EmailLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user_input: str
    reply_to: Optional[str] = Field(default=None)
    context: Optional[str] = Field(default=None)
    length: Optional[int] = Field(default=None)
    tone: str
    generated_email: str
    timestamp: str
