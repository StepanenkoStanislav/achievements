from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models import User, Achievement


class UserAchievementAssociation(Base):
    """Модель промежуточной таблицы для связи таблиц пользователей и достижений."""

    __tablename__ = "user_achievement_associations"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    achievement_id: Mapped[int] = mapped_column(ForeignKey("achievements.id"))
    timestamp: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    user: Mapped["User"] = relationship(back_populates="achievements")
    achievement: Mapped["Achievement"] = relationship(back_populates="users")

    __table_args__ = (
        UniqueConstraint("user_id", "achievement_id", name="unique_user_achievement"),
    )

    def __repr__(self):
        return (
            f"<User: {self.user}, id: {self.user_id} | "
            f"Achievement: {self.achievement}, id: {self.achievement_id}>"
        )
