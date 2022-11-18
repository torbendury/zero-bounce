"""Used for variables and core settings.
"""

import os


class Config:
    DB_USER = os.getenv("DB_USER", "DB_USER_MISSING")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "DB_PASSWORD_MISSING")
    DB_NAME = os.getenv("DB_NAME", "DB_NAME_MISSING")
    DB_HOST = os.getenv("DB_HOST", "DB_HOST_AND_PORT_MISSING")
    DB_CONFIG = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
