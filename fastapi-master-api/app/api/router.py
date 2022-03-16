from app.api import adapters, auth, machines, users
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(adapters.router)
api_router.include_router(auth.router)
api_router.include_router(machines.router)
api_router.include_router(users.router)
