"""
Application configuration.
"""

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.dirname(BASE_DIR)

DATABASE_PATH = os.path.join(
    PROJECT_ROOT,
    "frontend",
    "database",
    "futurefund.db",
)


class Settings:
    APP_NAME = "FutureFund AI"

    API_VERSION = "/api/v1"

    DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

    DEBUG = True


settings = Settings()