from sqlalchemy import Column, Integer, String
from .database import Base


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(60), nullable=False, unique=True)
    email = Column(String(60), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
