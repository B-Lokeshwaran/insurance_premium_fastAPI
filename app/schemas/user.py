from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    email: str
    password: str
    role: str


class Token(BaseModel):
    access_token: str
    token_type: str