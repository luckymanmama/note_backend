from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, JWTStrategy, CookieTransport

from .config import settings
from .dependencies import get_user_manager
from .models.users import User

cookie_transport = CookieTransport(cookie_name="note-backend", cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.SECRET_KEY, lifetime_seconds=3600)


auth_backend: AuthenticationBackend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_auth: FastAPIUsers = FastAPIUsers[User, int](get_user_manager, [auth_backend])
current_active_user = fastapi_auth.current_user(active=True)
