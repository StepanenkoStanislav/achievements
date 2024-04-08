from fastapi import APIRouter, Depends

from app.api_v1.dependencies import all_users
from app.models import User
from app.schemas.user import UserDB
from app.services import statistic

router = APIRouter()


@router.get("/max-achievements-count/", response_model=UserDB)
async def get_max_achievements_count_user(
    users: list[User] = Depends(all_users),
):
    """Получение пользователя с максимальным количеством достижений."""
    return await statistic.get_max_achievements_count_user(users)


@router.get("/max-achievements-points/", response_model=UserDB)
async def get_max_achievements_points_user(
    users: list[User] = Depends(all_users),
):
    """Получение пользователя с максимальным количеством очков достижений."""
    return await statistic.get_max_achievements_count_user(users)


@router.get("/max-difference-points/", response_model=UserDB)
async def get_max_difference_points_user(
    users: list[User] = Depends(all_users),
):
    """Получение пользователя с максимальной разницей очков достижений."""
    return await statistic.get_max_difference_points_user(users)


@router.get("/min-difference-points/", response_model=UserDB)
async def get_min_difference_points_user(
    users: list[User] = Depends(all_users),
):
    """Получение пользователя с минимальной разницей очков достижений."""
    return await statistic.get_min_difference_points_user(users)


@router.get("/achievements-week-for-a-row/", response_model=list[UserDB])
async def get_user_with_achievements_week_for_a_row(
    users: list[User] = Depends(all_users),
):
    """Получение пользователей, которым достижения выдавались 7 дней подряд."""
    return await statistic.get_achievements_week_for_a_row(users)
