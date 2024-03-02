from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer

from .blog import blog
from .user import user
from .auth import auth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/login", tags=["auth"])
api_router.include_router(blog.router, prefix="/blogs", tags=["blogs"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
