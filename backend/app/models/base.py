from sqlalchemy.orm import declarative_base, declared_attr, Mapped, mapped_column


class PreBase:
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"


Base = declarative_base(cls=PreBase)
