import pytest
from sqlalchemy.orm import sessionmaker, clear_mappers

from ddd_app.adapters.declarative_orm import start_declarative_mappers
from ddd_app.adapters.engines import mem_engine


@pytest.fixture
def in_memory_db():
    start_declarative_mappers(engine=mem_engine)
    return mem_engine


@pytest.fixture
def session(in_memory_db):
    yield sessionmaker(bind=in_memory_db)()