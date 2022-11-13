"""Used for variables and core settings.
"""

import os


class Config:
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "changeme")
    DB_NAME = os.getenv("DB_NAME", "postgres")
    DB_HOST = os.getenv("DB_HOST", "postgres:5432")
    DB_CONFIG = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
