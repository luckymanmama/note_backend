from typing import Optional
from urllib.request import Request

from fastapi_users import BaseUserManager, IntegerIDMixin
from ..config import settings
from ..models.users import User


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    """User management logic."""
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")
