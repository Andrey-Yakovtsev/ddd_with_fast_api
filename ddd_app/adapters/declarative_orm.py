from datetime import datetime
from sqlalchemy import Integer, String, func, JSON, ForeignKey
from sqlalchemy.orm import registry, DeclarativeBase, mapped_column, Mapped, \
    relationship

from ddd_app.adapters.engines import psql_engine

reg = registry()

class Base(DeclarativeBase):
    registry = reg


class User(Base):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(15))
    last_name: Mapped[str] = mapped_column(String(15))
    address_id: Mapped[int] = mapped_column(ForeignKey("address.id"))
    address: Mapped["Address"] = relationship(back_populates="users")
    joined: Mapped[datetime] = mapped_column(insert_default=func.now())
    birth_date: Mapped[datetime] = mapped_column(nullable=True)

class Address(Base):
    __tablename__ = "address"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    country: Mapped[str] = mapped_column(String(15))
    city: Mapped[str] = mapped_column(String(15))
    street: Mapped[str] = mapped_column(String(15))
    post_code: Mapped[int] = mapped_column(Integer())
    house: Mapped[int] = mapped_column(Integer())
    apartment: Mapped[int] = mapped_column(Integer())
    user: Mapped["User"] = relationship(back_populates="addresses")
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))


def start_declarative_mappers(engine):
    Base.metadata.create_all(engine)

