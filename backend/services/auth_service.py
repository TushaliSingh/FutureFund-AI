"""
Authentication business logic.
"""

from shared.auth import hash_password, verify_password

from backend.repositories import (
    create_user,
    get_user_by_email,
)


def signup_user(request):
    """
    Register a new user.
    """

    existing_user = get_user_by_email(request.email)

    if existing_user:
        return {
            "success": False,
            "message": "Email already registered."
        }

    # Hash password before saving
    request.password = hash_password(request.password)

    user = create_user(request)

    return {
        "success": True,
        "message": "User created successfully.",
        "user_id": user["id"],
    }


def login_user(request):
    """
    Authenticate user.
    """

    user = get_user_by_email(request.email)

    if user is None:
        return {
            "success": False,
            "message": "User not found."
        }

    stored_password = user["password"]

    if not verify_password(request.password, stored_password):
        return {
            "success": False,
            "message": "Invalid password."
        }

    return {
        "success": True,
        "message": "Login successful.",
        "user_id": user["id"],
    }