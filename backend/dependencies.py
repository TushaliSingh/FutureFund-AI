"""
Common FastAPI dependencies.
"""

from backend.database.database import get_connection


def get_db():
    """
    Provides database connection
    to API endpoints.
    """

    connection = get_connection()

    try:
        yield connection

    finally:
        connection.close()