from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import achievement as crud_achievement, user as crud_user
from app.api_v1.validators import (
    check_achievement_name_duplicate,
    check_user_already_have_achievement,
    check_user_exists,
    check_achievement_exists,
)
from app.core.db_helper import db_helper
from app.schemas.achievement import AchievementCreate, AchievementDB, AchievementSet
from app.schemas.user import UserDB

from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/", response_model=list[AchievementDB])
async def get_achievements(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Получение списка достижений."""
    return await crud_achievement.get_achievements(session)


@router.post("/", response_model=AchievementDB)
async def add_achievement(
    achievement: AchievementCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Добавление достижения."""
    await check_achievement_name_duplicate(achievement.name, session)
    return await crud_achievement.add_achievement(achievement, session)


@router.post("/set/", response_model=UserDB)
async def set_achievement(
    achievement_set_in: AchievementSet,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Присваивание достижения пользователю."""
    achievement_set = achievement_set_in.model_dump()
    user_id = achievement_set["user_id"]
    achievement_id = achievement_set["achievement_id"]

    user = await crud_user.get_user_by_id(user_id, session)
    check_user_exists(user, user_id)

    achievement = await crud_achievement.get_achievement_by_attr(
        "id", achievement_id, session
    )
    check_achievement_exists(achievement, achievement_id)

    check_user_already_have_achievement(user, achievement)
    return await crud_achievement.set_achievement_to_user(user, achievement, session)
