"""CRUD database utilities for archive categories and entries
"""

from sqlalchemy.orm import Session

from database import models

from schemas import CategoryBase, CategoryCreate, Category, EntryBase, EntryCreate, Entry

# import ..crud.models ..models, schemas


############### CATEGORIES


async def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return await db.query(models.Categories).offset(skip).limit(limit).all()


async def get_category(db: Session, category_id: int):
    return await db.query(models.Categories).filter(models.Categories.id == category_id).first()


async def create_category(db: Session, category: CategoryCreate):
    db_category = models.Categories(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return await db_category


async def delete_category():
    raise Exception("Implementation missing for deleting archive categories.")


async def update_category():
    raise Exception("Implementation missing for updating archive categories.")


############### ENTRIES


async def get_entries(db: Session, skip: int = 0, limit: int = 100):
    return await db.query(models.Entries).offset(skip).limit(limit).all()


async def get_entry(db: Session, entry_id: int):
    return await db.query(models.Entries).filter(models.Entries.id == entry_id).first()


async def get_category_entries(db: Session, category_id: int):
    return await db.query(models.Entries).filter(models.Entries.category_id == category_id).all()


async def create_entry(db: Session, entry: EntryCreate):
    db_entry = models.Entries(category_id=entry.category_id, visible_to_player=entry.visible_to_player, name=entry.name)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return await db_entry


async def delete_entry():
    raise Exception("Implementation missing for deleting archive category entries.")


async def update_entry():
    raise Exception("Implementation missing for updating archive category entries.")
