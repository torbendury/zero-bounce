from pydantic import BaseModel

# IMPORTANT!
# These are NOT the database models! These are pydantic models
# that allow FastAPI to do schema validation of Entry input!


class CategoryBase(BaseModel):
    """Base information for a category"""

    name: str


class CategoryCreate(CategoryBase):
    """Place for any additional needed information when creating a new category"""

    pass


class Category(CategoryBase):
    id: int
    # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict,
    # but an ORM model (or any other arbitrary object with attributes).
    # This way, instead of using `id = data["id"]`, you can get attributes with `id = data.id`.
    class Config:
        orm_mode = True


class EntryBase(BaseModel):
    name: str
    category_id: int
    visible_to_player: bool


class EntryCreate(EntryBase):
    pass


class Entry(EntryBase):
    id: int

    class Config:
        orm_mode = True
