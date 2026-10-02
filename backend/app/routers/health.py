from fastapi import APIRouter, Response, status
from app.schemas.health import HealthResponse
from app.services.health import get_system_health

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
async def check_health(response: Response) -> HealthResponse:
    """
    Health check endpoint verifying:
    - FastAPI app responsiveness
    - PostgreSQL connection status
    - Redis connection status
    """
    health = await get_system_health()
    if health.status != "ok":
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return health
