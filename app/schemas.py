from datetime import datetime, UTC
from typing import Optional

from sqlmodel import SQLModel, Field

# ------- user -------
class UserCreate(SQLModel):
    name: str
    username: str
    email: str
    password: str

class UserRead(SQLModel):
    id: int
    name: str
    username: str
    email: str

class UserCreateInternal(SQLModel):
    name: str
    username: str
    email: str
    hashed_password: str

# ------- email -------
class EmailRequest(SQLModel):
    user_input: str
    reply_to: Optional[str] = None
    context: Optional[str] = None
    length: int = 120
    tone: str = "formal"

class EmailResponse(SQLModel):
    generated_email: str

# ------- email log -------
class EmailLogCreate(SQLModel):
    user_id: int
    user_input: str
    reply_to: Optional[str] = None
    context: Optional[str] = None
    length: Optional[int] = None
    tone: Optional[str] = None
    generated_email: str
    timestamp: datetime = Field(
      default_factory=lambda: datetime.now(UTC)
    )

class EmailLogRead(SQLModel):
    user_id: int
    user_input: str
    reply_to: Optional[str]
    context: Optional[str]
    length: Optional[int]
    tone: Optional[str]
    generated_email: str
    timestamp: datetime
