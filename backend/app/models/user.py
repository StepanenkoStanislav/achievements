from enum import StrEnum
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy_utils import ChoiceType

from app.models.base import Base

if TYPE_CHECKING:
    from app.models import UserAchievementAssociation


class Languages(StrEnum):
    """Варианты для выбора языка пользователем."""

    ru = "ru"
    en = "en"


class User(Base):
    """Модель пользователя."""

    username: Mapped[str] = mapped_column(String(100), unique=True)
    language: Mapped[str] = mapped_column(ChoiceType(Languages, impl=String(length=2)))

    achievements: Mapped[list["UserAchievementAssociation"]] = relationship(
        back_populates="user",
    )

    def __repr__(self) -> str:
        return f"<User: {self.username}" f" | language: {self.language}>"
