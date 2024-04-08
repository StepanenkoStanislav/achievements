from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models import User, Achievement, UserAchievementAssociation
from app.schemas.achievement import AchievementCreate


async def get_achievements(session: AsyncSession) -> list[Achievement] | None:
    """Получение всех достижений."""
    stmt = select(Achievement).options(selectinload(Achievement.users))
    achievements = await session.scalars(stmt)
    return list(achievements.all())


async def get_achievement_by_attr(
    attr_name: str,
    attr_value: str | int,
    session: AsyncSession,
) -> Achievement | None:
    """Получение достижения по атрибуту."""
    attr = getattr(Achievement, attr_name)
    stmt = (
        select(Achievement)
        .options(
            selectinload(Achievement.users).joinedload(UserAchievementAssociation.user)
        )
        .where(attr == attr_value)
    )
    achievement = await session.scalar(stmt)
    return achievement


async def add_achievement(
    achievement_in: AchievementCreate,
    session: AsyncSession,
) -> Achievement:
    """Добавление достижения."""
    achievement = Achievement(**achievement_in.model_dump())
    session.add(achievement)
    await session.commit()
    await session.refresh(achievement)
    return achievement


async def set_achievement_to_user(
    user: User,
    achievement: Achievement,
    session: AsyncSession,
) -> User:
    """Присваивание достижения пользователю."""
    user.achievements.append(
        UserAchievementAssociation(achievement=achievement),
    )
    await session.commit()
    return user
