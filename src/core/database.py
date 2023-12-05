from typing import Any
from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy.sql import ClauseElement
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from .config import AppSettings
from typing import Optional

settings = AppSettings() # type: ignore

if settings.ENVIRONMENT == 'TESTING':
    engine = create_async_engine(str(settings.TEST_DATABASE_URL))
    print('make TEST db')
else:
    engine = create_async_engine(str(settings.DATABASE_URL))
    print('make PROD db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def fetch_one(select_query: ClauseElement) -> Optional[dict[str, Any]]:
    async with engine.begin() as conn:
        cursor: CursorResult = await conn.execute(select_query) # type: ignore
        return cursor.first()._asdict() if cursor.rowcount > 0 else None # type: ignore
    

async def fetch_all(select_query: ClauseElement) -> list[dict[str, Any]]:
    async with engine.begin() as conn:
        cursor: CursorResult = await conn.execute(select_query) # type: ignore
        return [r._asdict() for r in cursor.all()]


async def execute(select_query: ClauseElement) -> None:
    async with engine.begin() as conn:
        await conn.execute(select_query) # type: ignore