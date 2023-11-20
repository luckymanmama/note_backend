from datetime import datetime

from sqlalchemy.orm import DeclarativeBase
from typing import TYPE_CHECKING, Generic
from fastapi_users.models import ID
from sqlalchemy import Boolean, String, func
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
    """Base class for all models."""

    # Generate __tablename__ automatically
    @declared_attr.directive
    def __tablename__(cls) -> str:
        """Returns the lowercase name of the class as the table name."""
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True)


class TimestampMixin:
    """Mixin for adding timestamp columns."""
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(default=func.now(), onupdate=func.now())


class SQLAlchemyBaseUserTable(Generic[ID]):
    """Base SQLAlchemy users table definition."""

    __tablename__ = "user"

    if TYPE_CHECKING:  # pragma: no cover
        id: ID
        email: str
        hashed_password: str
        is_active: bool
        is_verified: bool
    else:
        email: Mapped[str] = mapped_column(
            String(length=320), unique=True, index=True, nullable=False
        )
        is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
        hashed_password: Mapped[str] = mapped_column(
            String(length=1024), nullable=False
        )
