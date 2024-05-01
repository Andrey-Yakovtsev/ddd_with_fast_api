from datetime import date

from pydantic import BaseModel, Field, PastDate



class Address(BaseModel):
    id: int
    post_code: int
    country: str = Field(max_length=15, min_length=2, pattern=r'^[a-zA-Z]+$')
    city: str = Field(max_length=15, min_length=2, pattern=r'^[a-zA-Z]+$')
    street: str = Field(max_length=15, min_length=2, pattern=r'^[a-zA-Z]+$')
    house: int
    apartment: int


class Birthday(BaseModel):
    date: PastDate

class User(BaseModel):
    id: int
    first_name: str = Field(max_length=15, min_length=2, pattern=r'^[a-zA-Z]+$')
    last_name: str = Field(max_length=15, min_length=2, pattern=r'^[a-zA-Z]+$')
    address: Address
    joined: date | None = None
    birth_date: Birthday | None = None
