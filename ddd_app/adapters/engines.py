from sqlalchemy import create_engine
from sqlalchemy.orm import Session

mem_engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
psql_engine = create_engine("postgresql+psycopg2://ddd:ddd@localhost/")


psql_session = Session(psql_engine)
