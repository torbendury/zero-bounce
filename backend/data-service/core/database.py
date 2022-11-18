from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import core.settings as appsettings

SQLALCHEMY_DATABASE_URL = appsettings.Config.DB_CONFIG
# "postgresql://user:password@postgresserver:port/database"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():  # pragma: no cover
    # yielding a database session. monkey-patched for unit and integration tests.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
