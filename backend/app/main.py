from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.ml_service import MLService
from app.api.api_v1.api import api_router
from app.database import engine
from app import models


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown events"""
    # Startup
    print("Starting up...")
    
    # Initialize ML service
    ml_service = MLService()
    await ml_service.initialize()
    app.state.ml_service = ml_service
    
    # Create tables
    models.Base.metadata.create_all(bind=engine)
    
    yield
    
    # Shutdown
    print("Shutting down...")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

# Set up CORS
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"], # restrict for produktion?
        allow_headers=["*"], # restrict for produktion?
    )

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
async def root():
    return {"message": "Restaurierungsentitaeten Annotation API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}