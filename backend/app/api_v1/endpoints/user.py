from fastapi import APIRouter, Depends

from app.api_v1.dependencies import user_by_id
from app.models import User
from app.schemas.achievement import AchievementToUser
from app.schemas.user import UserDB

router = APIRouter()


@router.get("/{user_id}/", response_model=UserDB)
async def get_user(
    user: User = Depends(user_by_id),
):
    """Получение пользователя."""
    return user


@router.get("/{user_id}/achievements/", response_model=list[AchievementToUser])
async def get_user_achievements(
    user: User = Depends(user_by_id),
):
    """Получение достижений пользователя."""
    return user.achievements
