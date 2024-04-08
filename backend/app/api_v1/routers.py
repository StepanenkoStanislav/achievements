from fastapi import APIRouter

from app.api_v1.endpoints import achievement_router, user_router, statistic_router
from app.core.config import settings

api_v1_router = APIRouter(prefix=settings.api_v1_prefix)

api_v1_router.include_router(
    user_router,
    prefix="/users",
    tags=["Users"],
)
api_v1_router.include_router(
    achievement_router,
    prefix="/achievements",
    tags=["Achievements"],
)
api_v1_router.include_router(
    statistic_router,
    prefix="/statistics",
    tags=["Statistics"],
)
