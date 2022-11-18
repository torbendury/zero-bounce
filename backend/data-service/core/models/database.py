from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base


class Categories(Base):
    __tablename__ = "categories"
    # this emits 'id' as a SERIAL type with auto-increment sequence
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False, unique=True)
    # this is great magic, it lets you create a one-to-many semantic
    # by accessing this attribute, SQLAlchemy retrieves the entries
    # for a given category - and vice versa (see below)!
    entries = relationship("Entries", back_populates="category")


class Entries(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    visible_to_player = Column(Boolean, default=False, nullable=False)
    name = Column(String, index=True, nullable=False)

    category = relationship("Categories", back_populates="entries")
