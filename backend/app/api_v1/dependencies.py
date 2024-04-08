from typing import Annotated

from fastapi import Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api_v1.validators import check_user_exists
from app.crud.user import get_user_by_id, get_all_users
from app.core.db_helper import db_helper
from app.models import User


async def user_by_id(
    user_id: Annotated[int, Path(ge=1)],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> User:
    """Получение пользователя по id."""
    user = await get_user_by_id(user_id, session)
    check_user_exists(user, user_id)
    return user


async def all_users(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> list[User]:
    """Получение всех пользователей."""
    return await get_all_users(session)
