"""
Repository for user database operations.
"""

from backend.database.database import get_connection


def create_user(request):
    """
    Save a new user to the database.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users (
            name,
            email,
            password,
            age,
            income,
            risk,
            monthly_expenses,
            monthly_savings,
            financial_goal,
            investment_experience
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            request.name,
            request.email,
            request.password,
            request.age,
            request.income,
            request.risk,
            request.monthly_expenses,
            request.monthly_savings,
            request.financial_goal,
            request.investment_experience,
        ),
    )

    conn.commit()

    cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        (request.email,),
    )

    user = cursor.fetchone()

    conn.close()

    return user


def get_user_by_email(email):
    """
    Fetch a user by email.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,),
    )

    user = cursor.fetchone()

    conn.close()

    return user