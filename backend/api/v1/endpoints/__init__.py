from .investments import router as investment_router
from .auth import router as auth_router

__all__ = [
    "investment_router",
    "auth_router",
]