from app.api import (
    users,
    auth
)

from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(auth.router)