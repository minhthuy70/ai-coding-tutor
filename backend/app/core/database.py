from typing import Tuple, Optional
try:
    from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
    from sqlalchemy import text
except Exception:
    create_async_engine, async_sessionmaker, AsyncSession, text = None, None, None, None
from app.core.config import settings

engine = None
AsyncSessionLocal = None

try:
    engine = create_async_engine(
        settings.DATABASE_URL,
        echo=False,
        pool_pre_ping=True,
        pool_size=10,
        max_overflow=20,
    )

    AsyncSessionLocal = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
    )
except Exception:
    pass


async def check_database_connection() -> Tuple[bool, Optional[str]]:
    """Test PostgreSQL connection by executing a simple SELECT 1 query."""
    if engine is None:
        return False, "Database driver (asyncpg) not installed or engine not initialized"
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return True, "connected"
    except Exception as exc:
        return False, str(exc)
