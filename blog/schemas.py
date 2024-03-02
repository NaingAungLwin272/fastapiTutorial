from asyncio import streams
from pydantic import BaseModel


class BlogModel(BaseModel):
    title: str
    description: str


class ShowBlogModel(BaseModel):
    id: int
    title: str
    description: str


class User(BaseModel):
    username: str
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class ShowUser(BaseModel):
    id: int
    username: str
    email: str
