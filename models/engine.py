from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from core import CONFIG


ENGINE = create_async_engine(f'postgresql+asyncpg://{CONFIG.DATABASE}')
SYNC_ENGINE = create_engine(f'postgresql://{CONFIG.DATABASE}')
Session = sessionmaker(bind=SYNC_ENGINE)


def create_async_session(func):
    async def wrapper(**kwargs):
        async with AsyncSession(bind=ENGINE) as session:
            return await func(**kwargs, session=session)
    return wrapper


def create_sync_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            return func(**kwargs, session=session)
    return wrapper

