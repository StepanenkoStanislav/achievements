from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models import User, UserAchievementAssociation


async def get_all_users(
    session: AsyncSession,
) -> list[User]:
    """Получение всех пользователей."""
    stmt = select(User).options(
        selectinload(User.achievements).joinedload(
            UserAchievementAssociation.achievement
        )
    )
    users = await session.scalars(stmt)
    return list(users.all())


async def get_user_by_id(
    user_id: int,
    session: AsyncSession,
) -> User | None:
    """Получение пользователя по id."""
    stmt = (
        select(User)
        .options(
            selectinload(User.achievements).joinedload(
                UserAchievementAssociation.achievement
            ),
        )
        .where(User.id == user_id)
    )
    user = await session.scalar(stmt)
    return user
