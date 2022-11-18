from fastapi import APIRouter, Response, status, Depends, HTTPException
from sqlalchemy.orm import Session
import core.schemas.schema as schemas
from v1.crud import archive
from core.database import get_db

router = APIRouter()

# CATEGORIES


@router.get("/categories/", status_code=status.HTTP_200_OK, response_model=list[schemas.Category])
async def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_categories = archive.get_categories(db=db, skip=skip, limit=limit)
    return db_categories


@router.get("/categories/{category_id}", status_code=status.HTTP_200_OK, response_model=schemas.Category)
async def read_category(category_id: int, response: Response, db: Session = Depends(get_db)):
    db_category = archive.get_category(db=db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return db_category


@router.post("/categories/", status_code=status.HTTP_201_CREATED, response_model=schemas.Category)
async def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = archive.get_category_by_name(db=db, category_name=category.name)
    if db_category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category already exists")
    return archive.create_category(db=db, category=category)


@router.delete("/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category_by_id(category_id: int, db: Session = Depends(get_db)):
    db_category = archive.delete_category(db=db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/categories/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category_by_name(category: schemas.CategoryDelete, db: Session = Depends(get_db)):
    db_category = archive.delete_category_by_name(db=db, category_name=category.name)
    if db_category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/categories/{category_id}", status_code=status.HTTP_200_OK, response_model=schemas.Category)
async def update_category(category_id: int, category: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    db_category = archive.update_category(db=db, category_id=category_id, category=category)
    if db_category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return db_category


# ENTRIES


@router.get("/categories/{category_id}/entries", status_code=status.HTTP_200_OK, response_model=list[schemas.Entry])
async def read_category_entries(category_id: int, response: Response, db: Session = Depends(get_db)):
    db_entries = archive.get_category_entries(db=db, category_id=category_id)
    if db_entries is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return db_entries


@router.get("/entries/{entry_id}", status_code=status.HTTP_200_OK, response_model=schemas.Entry)
async def read_category_entry(entry_id: int, response: Response, db: Session = Depends(get_db)):
    db_entry = archive.get_entry(db=db, entry_id=entry_id)
    if db_entry is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entry not found")
    return db_entry


@router.get("/entries", status_code=status.HTTP_200_OK, response_model=list[schemas.Entry])
async def read_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_entries = archive.get_entries(db=db, skip=skip, limit=limit)
    return db_entries


@router.delete("/entries/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    db_entry = archive.delete_entry(db=db, entry_id=entry_id)
    if db_entry is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entry not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/entries/{entry_id}", status_code=status.HTTP_200_OK, response_model=schemas.Entry)
async def update_entry(entry_id: int, entry: schemas.EntryUpdate, db: Session = Depends(get_db)):
    db_entry = archive.update_entry(db=db, entry_id=entry_id, entry=entry)
    if db_entry is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entry not found")
    return db_entry


# will read post documents for entries from NoSQL, to be done later
@router.get("/categories/{category_id}/entries/{entry_id}/post", status_code=status.HTTP_200_OK)
async def read_category_entry_post(category_id: int, entry_id: int, response: Response):
    return {}
