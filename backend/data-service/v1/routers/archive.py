from fastapi import APIRouter, Response, status, Depends, HTTPException
from sqlalchemy.orm import Session
import core.schemas.schema as schemas
from v1.crud import archive
from core import database

router = APIRouter()

# CATEGORIES


@router.get("/categories", status_code=200, response_model=list[schemas.Category])
async def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    db_categories = archive.get_categories(db=db, skip=skip, limit=limit)
    print(db_categories)
    return db_categories


@router.get("/categories/{category_id}", status_code=200, response_model=schemas.Category)
async def read_category(category_id: int, response: Response, db: Session = Depends(database.get_db)):
    db_category = archive.get_category(db=db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return db_category


@router.post("/categories/", response_model=schemas.Category)
async def create_category(category: schemas.CategoryCreate, db: Session = Depends(database.get_db)):
    db_category = archive.create_category(db=db, category=category)
    return db_category


# ENTRIES


@router.get("/categories/{category_id}/entries", status_code=200, response_model=list[schemas.Entry])
async def read_category_entries(category_id: int, response: Response, db: Session = Depends(database.get_db)):
    db_entries = archive.get_category_entries(db=db, category_id=category_id)
    return db_entries


@router.get("/entries/{entry_id}", status_code=200, response_model=schemas.Entry)
async def read_category_entry(entry_id: int, response: Response, db: Session = Depends(database.get_db)):
    db_entry = archive.get_entry(db=db, entry_id=entry_id)
    if db_entry is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entry not found")
    return db_entry


@router.get("/entries", status_code=200, response_model=list[schemas.Entry])
async def read_entries(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    db_entries = archive.get_entries(db=db, skip=skip, limit=limit)
    return db_entries


# will read post documents for entries from NoSQL, to be done later
@router.get("/categories/{category_id}/entries/{entry_id}/post", status_code=200)
async def read_category_entry_post(category_id: int, entry_id: int, response: Response):
    return {}
