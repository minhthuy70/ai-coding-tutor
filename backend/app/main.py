from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import engine
from app.core.redis import redis_client
from app.routers import health_router, tutor_router, knowledge_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    yield
    # Cleanup / Shutdown actions
    if engine is not None:
        try:
            await engine.dispose()
        except Exception:
            pass
    if redis_client is not None and hasattr(redis_client, "aclose"):
        try:
            await redis_client.aclose()
        except Exception:
            pass


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0",
    description="Backend API for AI-Powered Coding Tutor & Auto-Grader",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# Setup CORS
origins = settings.BACKEND_CORS_ORIGINS if isinstance(settings.BACKEND_CORS_ORIGINS, list) else ["*"]
if not origins or origins == [""]:
    origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if "*" not in origins else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Routers
# /api and /api/v1 prefix compatibility
app.include_router(health_router, prefix="/api")
app.include_router(tutor_router, prefix="/api")
app.include_router(knowledge_router, prefix="/api")
if settings.API_V1_STR != "/api":
    app.include_router(health_router, prefix=settings.API_V1_STR)
    app.include_router(tutor_router, prefix=settings.API_V1_STR)
    app.include_router(knowledge_router, prefix=settings.API_V1_STR)
app.include_router(health_router, prefix="/api/v1")
app.include_router(tutor_router, prefix="/api/v1")
app.include_router(knowledge_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {
        "name": settings.PROJECT_NAME,
        "version": "0.1.0",
        "status": "running",
        "docs": "/docs",
        "health": f"{settings.API_V1_STR}/health"
    }
