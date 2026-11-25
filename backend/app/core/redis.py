from typing import Tuple, Optional
try:
    import redis.asyncio as aioredis
except Exception:
    aioredis = None
from app.core.config import settings

redis_client = None
try:
    redis_client = aioredis.from_url(
        settings.REDIS_URL,
        encoding="utf-8",
        decode_responses=True,
        socket_timeout=3.0,
        socket_connect_timeout=3.0,
    )
except Exception:
    pass


async def check_redis_connection() -> Tuple[bool, Optional[str]]:
    """Test Redis connection by executing ping()."""
    if redis_client is None:
        return False, "Redis client not initialized"
    try:
        response = await redis_client.ping()
        if response:
            return True, "connected"
        return False, "unexpected ping response"
    except Exception as exc:
        return False, str(exc)
