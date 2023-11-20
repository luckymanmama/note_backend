from typing import Generator, AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession, async_session
from sqlalchemy.orm import sessionmaker

from .config import settings

engine = create_async_engine(
    f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncSession:
    """Dependency for getting async session"""
    async with async_session_maker() as session:
        yield session
