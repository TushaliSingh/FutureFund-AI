"""
Database operations for investments.
"""

from backend.database.database import get_connection


def save_investment(
    user_id,
    investment_type,
    amount
):
    """
    Save investment record.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO investments
        (
            user_id,
            investment_type,
            amount
        )
        VALUES (?, ?, ?)
        """,
        (
            user_id,
            investment_type,
            amount,
        )
    )

    connection.commit()

    connection.close()