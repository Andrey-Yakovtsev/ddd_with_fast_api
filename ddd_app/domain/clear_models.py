from dataclasses import dataclass
from datetime import date


from ddd_app.adapters.declarative_orm import start_declarative_mappers
from ddd_app.adapters.engines import psql_engine

@dataclass(frozen=True, slots=True)
class Address:
    id: int
    post_code: int
    country: str
    city: str
    street: str
    house: int
    apartment: int


@dataclass(frozen=True, slots=True)
class Birthday:
    date: date

@dataclass(frozen=True, slots=True)
class User:
    id: int
    first_name: str
    last_name: str
    address: Address
    joined: date | None = None
    birth_date: Birthday | None = None


# start_declarative_mappers(engine=psql_engine)

addr_1 = Address(id=3, country="RUS", city="Moscow",
                 street="BakerStreet", post_code=12345, house=1, apartment=3)

print(addr_1)

