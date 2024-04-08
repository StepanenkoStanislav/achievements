from datetime import datetime

from pydantic import BaseModel, ConfigDict, model_validator

from app.models.user import Languages
from app.schemas.achievement import AchievementDB


class UserAchievementSchema(AchievementDB):
    """Схема для присвоенных пользователю достижений при получении пользователя."""

    model_config = ConfigDict(from_attributes=True)
    timestamp: datetime

    @model_validator(mode="before")
    @classmethod
    def validate(cls, values):
        values.achievement.timestamp = values.timestamp
        return values.achievement


class UserDB(BaseModel):
    """Схема для пользователя из БД."""

    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    language: Languages
    achievements: list[UserAchievementSchema]
