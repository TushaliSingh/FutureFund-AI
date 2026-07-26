"""
Authentication API endpoints.
"""

from fastapi import APIRouter, HTTPException

from backend.schemas import (
    SignupRequest,
    LoginRequest,
    AuthResponse,
)

from backend.services import (
    signup_user,
    login_user,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/signup",
    response_model=AuthResponse,
)
def signup(request: SignupRequest):

    result = signup_user(request)

    if not result["success"]:
        raise HTTPException(
            status_code=400,
            detail=result["message"],
        )

    return AuthResponse(
        message=result["message"],
        user_id=result["user_id"],
    )


@router.post(
    "/login",
    response_model=AuthResponse,
)
def login(request: LoginRequest):

    result = login_user(request)

    if not result["success"]:
        raise HTTPException(
            status_code=401,
            detail=result["message"],
        )

    return AuthResponse(
        message=result["message"],
        user_id=result["user_id"],
    )