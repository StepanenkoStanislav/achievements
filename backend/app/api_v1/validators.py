from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.achievement import get_achievement_by_attr
from app.models import User, Achievement


async def check_achievement_name_duplicate(
    name: str,
    session: AsyncSession,
) -> None:
    """Проверка уникальности названия достижения."""
    if await get_achievement_by_attr("name", name, session):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Achievement with name {name} already exists",
        )


def check_achievement_exists(
    achievement: Achievement | None,
    achievement_id: int,
) -> None:
    """Проверка существования достижения."""
    if not achievement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Achievement {achievement_id} not found",
        )


def check_user_already_have_achievement(
    user: User,
    achievement: Achievement,
) -> None:
    """Проверка, что пользователь не получал присваиваемое достижение ранее."""
    user_achievements = [association.achievement for association in user.achievements]
    if achievement in user_achievements:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"User {user.username} already have achievement {achievement.name}",
        )


def check_user_exists(
    user: User | None,
    user_id: int,
) -> None:
    """Проверка существования пользователя."""
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} not found",
        )
