from fastapi import APIRouter

from backend.api.v1.endpoints import (
    investment_router,
    auth_router,
)

api_router = APIRouter()

api_router.include_router(investment_router)
api_router.include_router(auth_router)