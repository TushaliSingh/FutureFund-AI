"""
Database configuration and connection handling.
"""

import sqlite3

from backend.core.config import settings


def get_connection():
    """
    Creates and returns a database connection.
    """

    connection = sqlite3.connect(
        settings.DATABASE_URL.replace(
            "sqlite:///",
            ""
        )
    )

    connection.row_factory = sqlite3.Row

    return connection
    