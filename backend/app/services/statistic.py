from math import inf

from app.models import User


async def get_max_achievements_count_user(users: list[User]) -> User:
    """Получение пользователя с максимальным количеством достижений."""
    max_achievements_count = 0
    result = None
    for user in users:
        if len(user.achievements) > max_achievements_count:
            max_achievements_count = len(user.achievements)
            result = user
    return result or []


async def get_max_achievements_points_user(users: list[User]) -> User:
    """Получение пользователя с максимальным количеством очков достижений."""
    max_achievements_points = 0
    result = None
    for user in users:
        points_sum = sum([a.achievement.points for a in user.achievements])
        if points_sum > max_achievements_points:
            max_achievements_points = points_sum
            result = user
    return result


async def get_max_difference_points_user(users: list[User]) -> User:
    """Получение пользователя с максимальной разницей очков достижений."""
    max_difference = 0
    result = None
    for user in users:
        if len(user.achievements) <= 1:
            continue
        max_points = max(
            user.achievements, key=lambda a: a.achievement.points
        ).achievement.points
        min_points = min(
            user.achievements, key=lambda a: a.achievement.points
        ).achievement.points
        difference = max_points - min_points
        if difference >= max_difference:
            max_difference = difference
            result = user
    return result


async def get_min_difference_points_user(users: list[User]) -> User:
    """Получение пользователя с минимальной разницей очков достижений."""
    min_difference = inf
    result = None
    for user in users:
        if len(user.achievements) <= 1:
            continue
        max_points = max(
            user.achievements, key=lambda a: a.achievement.points
        ).achievement.points
        min_points = min(
            user.achievements, key=lambda a: a.achievement.points
        ).achievement.points
        difference = max_points - min_points
        if difference <= min_difference:
            min_difference = difference
            result = user
    return result


async def get_achievements_week_for_a_row(
    users: list[User],
) -> list[User]:
    """Получение пользователей, которым достижения выдавались 7 дней подряд."""
    result = []
    for user in users:
        dates = [achievement.timestamp.date() for achievement in user.achievements]
        dates.sort()
        i = 1
        counter = 1
        while i < len(dates):
            date_difference = dates[i] - dates[i - 1]
            if date_difference.days == 1:
                counter += 1
                if counter == 7:
                    result.append(user)
                    break
            else:
                counter = 1
            i += 1
    return result
