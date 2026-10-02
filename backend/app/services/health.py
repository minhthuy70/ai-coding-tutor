import asyncio
from app.core.database import check_database_connection
from app.core.redis import check_redis_connection
from app.schemas.health import HealthResponse


async def get_system_health() -> HealthResponse:
    """Check health of FastAPI application, PostgreSQL, and Redis."""
    # Run DB and Redis checks concurrently
    db_task = asyncio.create_task(check_database_connection())
    redis_task = asyncio.create_task(check_redis_connection())

    (db_ok, db_msg), (redis_ok, redis_msg) = await asyncio.gather(db_task, redis_task)

    db_status = "connected" if db_ok else f"disconnected ({db_msg})"
    redis_status = "connected" if redis_ok else f"disconnected ({redis_msg})"

    overall_status = "ok" if (db_ok and redis_ok) else "degraded"

    return HealthResponse(
        status=overall_status,
        database=db_status,
        redis=redis_status,
        environment="development"
    )
