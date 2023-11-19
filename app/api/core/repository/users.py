import uuid

from fastapi_users import BaseUserManager, UUIDIDMixin

from ..models.users import User


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    """User management logic."""
    pass
