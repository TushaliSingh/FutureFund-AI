"""
Pydantic schemas for FutureFund AI.
"""

from .investment import SIPRequest, SIPResponse
from .auth import SignupRequest, LoginRequest, AuthResponse


__all__ = [
    "SIPRequest",
    "SIPResponse",
    "SignupRequest",
    "LoginRequest",
    "AuthResponse",
]