"""CRUD database utilities for archive categories and entries
"""

from sqlalchemy.orm import Session

from core.models import database as models

import core.schemas.schema as schemas

# import CategoryBase, CategoryCreate, Category, EntryBase, EntryCreate, Entry

# import ..crud.models ..models, schemas


############### CATEGORIES


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Categories).offset(skip).limit(limit).all()


def get_category(db: Session, category_id: int):
    return db.query(models.Categories).filter(models.Categories.id == category_id).first()


def get_category_by_name(db: Session, category_name: str):
    return db.query(models.Categories).filter(models.Categories.name == category_name).first()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Categories(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int):
    db_category_query = db.query(models.Categories).filter(models.Categories.id == category_id)
    db_category = db_category_query.first()
    if db_category is None:
        return None
    db_category_query.delete(synchronize_session=False)
    db.commit()
    return True


def delete_category_by_name(db: Session, category_name: str):
    db_category_query = db.query(models.Categories).filter(models.Categories.name == category_name)
    db_category = db_category_query.first()
    if db_category is None:
        return None
    db_category_query.delete(synchronize_session=False)
    db.commit()
    return True


def update_category(db: Session, category_id: int, category: schemas.CategoryUpdate):
    db_category_query = db.query(models.Categories).filter(models.Categories.id == category_id)
    db_category = db_category_query.first()
    if db_category is None:
        return None
    db_category_query.update(category.dict(), synchronize_session=False)
    db.commit()
    return get_category(db=db, category_id=category_id)


############### ENTRIES


def get_entries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Entries).offset(skip).limit(limit).all()


def get_entry(db: Session, entry_id: int):
    return db.query(models.Entries).filter(models.Entries.id == entry_id).first()


def get_category_entries(db: Session, category_id: int):
    db_category = get_category(db=db, category_id=category_id)
    if db_category is None:
        return None
    return db.query(models.Entries).filter(models.Entries.category_id == category_id).all()


def create_entry(db: Session, entry: schemas.EntryCreate):
    db_entry = models.Entries(category_id=entry.category_id, visible_to_player=entry.visible_to_player, name=entry.name)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


def delete_entry(db: Session, entry_id: int):
    db_entry_query = db.query(models.Entries).filter(models.Entries.id == entry_id)
    db_entry = db_entry_query.first()
    if db_entry is None:
        return None
    db_entry_query.delete(synchronize_session=False)
    db.commit()
    return True


def update_entry(db: Session, entry_id: int, entry: schemas.EntryUpdate):
    db_entry_query = db.query(models.Entries).filter(models.Entries.id == entry_id)
    db_entry = db_entry_query.first()
    if db_entry is None:
        return None
    db_entry_query.update(entry.dict(), synchronize_session=False)
    db.commit()
    return get_entry(db=db, entry_id=entry_id)
