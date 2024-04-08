from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import settings


class DatabaseHelper:
    """Подключение к БД. Создание движка и фабрики сессии."""

    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        """На основе фабрики сессии создаётся scoped_session."""

        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        """Scoped session используется для подключения к БД
        во время создания запросов."""

        session = self.get_scoped_session()
        async with session() as async_session:
            yield async_session
            await session.remove()


db_helper = DatabaseHelper(url=settings.db.db_url)
