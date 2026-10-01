from typing import Tuple, Optional
import redis.asyncio as aioredis
from app.core.config import settings

redis_client = aioredis.from_url(
    settings.REDIS_URL,
    encoding="utf-8",
    decode_responses=True,
    socket_timeout=3.0,
    socket_connect_timeout=3.0,
)


async def check_redis_connection() -> Tuple[bool, Optional[str]]:
    """Test Redis connection by executing ping()."""
    try:
        response = await redis_client.ping()
        if response:
            return True, "connected"
        return False, "unexpected ping response"
    except Exception as exc:
        return False, str(exc)
