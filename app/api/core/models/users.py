from typing import List

from sqlalchemy.orm import relationship, Mapped
from .base import Base, TimestampMixin, SQLAlchemyBaseUserTable
from . import notes


class User(SQLAlchemyBaseUserTable, TimestampMixin, Base):
    """Base User model with UUID as primary key and timestamp columns."""
    notes: Mapped[List["notes.Note"]] = relationship(back_populates="user")
    is_active: Mapped
