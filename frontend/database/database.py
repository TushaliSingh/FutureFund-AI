import sqlite3
import os

# ---------------------------------------------------
# Database Path
# ---------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_NAME = os.path.join(BASE_DIR, "futurefund.db")


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_database():

    conn = get_connection()
    cursor = conn.cursor()

    # ---------------- Users Table ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        email TEXT UNIQUE,

        password TEXT,

        age INTEGER,

        income REAL,

        risk TEXT,

        monthly_expenses REAL,

        monthly_savings REAL,

        financial_goal TEXT,

        investment_experience TEXT

    )
    """)

    # ---------------- Investment History Table ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS investment_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        feature TEXT,

        result TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(user_id) REFERENCES users(id)

    )
    """)

    conn.commit()
    conn.close()


# ---------------------------------------------------
# User Functions
# ---------------------------------------------------

def add_user(
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
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (
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
    )

    conn.commit()
    conn.close()


def get_user(email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


# ---------------------------------------------------
# Investment History
# ---------------------------------------------------

def save_history(user_id, feature, result):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO investment_history
        (user_id, feature, result)

        VALUES (?, ?, ?)
        """,
        (
            user_id,
            feature,
            result
        )
    )

    conn.commit()
    conn.close()


def get_history(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT feature, result, created_at
        FROM investment_history
        WHERE user_id=?
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    history = cursor.fetchall()

    conn.close()

    return history


create_database()