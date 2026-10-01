from typing import Optional
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(..., description="Overall system health status ('ok' or 'degraded')")
    database: str = Field(..., description="PostgreSQL connection status")
    redis: str = Field(..., description="Redis connection status")
    environment: Optional[str] = Field(default="development", description="Current environment")
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "ok",
                "database": "connected",
                "redis": "connected",
                "environment": "development"
            }
        }
