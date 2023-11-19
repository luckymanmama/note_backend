from fastapi import APIRouter

from .users import router as users_router
from .notes import router as rates_router

api_router = APIRouter()


api_router.include_router(users_router, prefix="/auth", tags=["auth"])
api_router.include_router(rates_router, prefix="/notes", tags=["notes"])
