from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, registry

from ddd_app.adapters.engines import psql_engine
from ddd_app.domain import models

metadata = registry().metadata


addresses = Table(
    'addresses',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('country', String(50)),
    Column('city', String(50)),
    Column('street', String(50)),
    Column('post_code', Integer()),
    Column('house', Integer()),
    Column('apartment', Integer()),
   )

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
    Column("birth_date", Date, nullable=True),
    Column("joined", Date, nullable=True),
    Column("address_id", Integer, ForeignKey("addresses.id"), nullable=True),
)



# metadata.create_all(psql_engine)