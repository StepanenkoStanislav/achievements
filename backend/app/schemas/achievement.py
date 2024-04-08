from datetime import datetime
from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, conint, ConfigDict, model_validator, Field


class AchievementCreate(BaseModel):
    """Схема для создания достижения."""

    name: Annotated[str, MinLen(3), MaxLen(100)]
    points: conint(gt=0)
    description_ru: Annotated[str, MinLen(3)]
    description_en: Annotated[str, MinLen(3)]


class AchievementDB(AchievementCreate):
    """Схема для достижений из базы данных."""

    model_config = ConfigDict(from_attributes=True)
    id: int


class AchievementSet(BaseModel):
    """Схема для присваивания достижения пользователю."""

    user_id: conint(gt=0)
    achievement_id: conint(gt=0)


class AchievementToUser(AchievementDB):
    """Схема для присвоенных пользователю достижений на выбранном языке."""

    model_config = ConfigDict(from_attributes=True)
    description: str
    timestamp: datetime
    description_ru: str = Field(exclude=True)
    description_en: str = Field(exclude=True)

    @model_validator(mode="before")
    @classmethod
    def validate(cls, values):
        values.achievement.timestamp = values.timestamp
        values.achievement.description = (
            values.achievement.description_ru
            if values.user.language == "ru"
            else values.achievement.description_en
        )
        return values.achievement
