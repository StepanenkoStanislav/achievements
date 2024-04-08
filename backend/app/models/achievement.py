from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, Integer, String, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.models.base import Base

if TYPE_CHECKING:
    from app.models import UserAchievementAssociation


class Achievement(Base):
    """Модель достижения."""

    name: Mapped[str] = mapped_column(String(100), unique=True)
    description_ru: Mapped[str] = mapped_column(Text)
    description_en: Mapped[str] = mapped_column(Text)
    points: Mapped[int] = mapped_column(Integer)

    users: Mapped[list["UserAchievementAssociation"]] = relationship(
        back_populates="achievement",
    )

    __table_args__ = (CheckConstraint(points > 0, name="check_points_positive"),)

    def __repr__(self) -> str:
        return f"<Achievement: {self.name} | points: {self.points}>"
