from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from . import users
from .base import Base, TimestampMixin


class Note(Base, TimestampMixin):
    title: Mapped[str]
    body: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["users.User"] = relationship(back_populates="notes")
