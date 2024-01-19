from fastapi import APIRouter

from .blog import blog
from .user import user

api_router = APIRouter()

api_router.include_router(blog.router, prefix="/blogs", tags=["blogs"])
api_router.include_router(user.router, prefix="/users", tags=["users"])