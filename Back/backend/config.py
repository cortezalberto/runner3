"""
Centralized configuration for the application

IMPORTANT: Render.com version - Docker-related settings removed
"""
import os
from typing import List


class Settings:
    """Application settings with environment variable support"""

    # Database (Render provides DATABASE_URL automatically)
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://playground:playground@localhost:5432/playground"
    )

    # Redis (Use Upstash Redis URL for Render)
    REDIS_URL: str = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379/0"
    )

    # API
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))

    # CORS - Allow Vercel frontend
    _cors_origins = os.getenv(
        "CORS_ORIGINS",
        "http://localhost:5173,http://localhost:5174,https://front-eight-rho-61.vercel.app"
    )
    CORS_ORIGINS: List[str] = [origin.strip() for origin in _cors_origins.split(",")]

    # Allow all origins in development (set to false in production)
    CORS_ALLOW_ALL_ORIGINS: bool = os.getenv("CORS_ALLOW_ALL_ORIGINS", "false").lower() == "true"

    # Limits
    MAX_CODE_LENGTH: int = int(os.getenv("MAX_CODE_LENGTH", "50000"))
    MAX_SUBMISSION_POLL_ATTEMPTS: int = int(os.getenv("MAX_POLL_ATTEMPTS", "30"))
    POLL_INTERVAL_SEC: float = float(os.getenv("POLL_INTERVAL_SEC", "1.0"))

    # Paths
    PROBLEMS_DIR: str = os.getenv("PROBLEMS_DIR", "backend/problems")
    BACKEND_DIR: str = os.getenv("BACKEND_DIR", "backend")

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


# Singleton instance
settings = Settings()
