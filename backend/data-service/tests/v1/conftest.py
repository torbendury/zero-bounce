import pytest
from core.database import Base, get_db
from core import database
from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy_utils import create_database, database_exists
from v1.crud.archive import create_category, create_entry
from core.schemas.schema import CategoryCreate, EntryCreate
import os


database.SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"


class Config:
    DB_CONFIG = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"


@pytest.fixture(scope="function")
def db_engine():
    print("DB engine creation.")
    engine = create_engine(database.SQLALCHEMY_DATABASE_URL)

    if not database_exists:
        create_database(engine.url)
    print("Dropping all tables.")
    Base.metadata.drop_all(bind=engine)
    print("Recreating all tables.")
    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope="function")
def db(db_engine):
    print("Creating db session.")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

    db = SessionLocal()

    app.dependency_overrides[get_db] = lambda: db
    print("Yielding DB")
    yield db
    print("Rolling back everything uncommitted.")
    db.rollback()
    print("Closing DB connection.")
    db.close()


@pytest.fixture(scope="function")
def client(db):
    print("Generating application client.")
    print("Overwriting db settings.")
    app.dependency_overrides[get_db] = lambda: db

    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def categories(db):
    print("Running categories fixture.")
    create_category(db=db, category=CategoryCreate(name="place"))
    create_category(db=db, category=CategoryCreate(name="vehicle"))


@pytest.fixture(scope="function")
def categories_entries(db):
    print("Running categories and entries fixture.")
    # id 1
    create_category(db=db, category=CategoryCreate(name="place"))
    # id 2
    create_category(db=db, category=CategoryCreate(name="vehicle"))
    # id 1, 2, 3, 4
    create_entry(db=db, entry=EntryCreate(name="Pirmasens", category_id=1, visible_to_player=True))
    create_entry(db=db, entry=EntryCreate(name="Berlin", category_id=1, visible_to_player=True))
    create_entry(db=db, entry=EntryCreate(name="Coach", category_id=2, visible_to_player=True))
    create_entry(db=db, entry=EntryCreate(name="Hovercraft", category_id=2, visible_to_player=True))
