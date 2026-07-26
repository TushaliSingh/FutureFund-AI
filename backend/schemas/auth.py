from pydantic import BaseModel, EmailStr, Field


class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=6)

    age: int
    income: float
    risk: str

    monthly_expenses: float
    monthly_savings: float

    financial_goal: str
    investment_experience: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class AuthResponse(BaseModel):
    message: str
    user_id: int