from fastapi import FastAPI

from ddd_app.adapters.engines import psql_session
from ddd_app.adapters.repository import SqlAlchemyRepository
from ddd_app.domain.models import User

app = FastAPI()
repo = SqlAlchemyRepository(psql_session)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user/{id}")
async def get_user(id: int):
    user = repo.get(id)
    return {"user": user}


@app.post("/createuser")
async def create_user(user: User):
    print(user)
    repo.add(user)
    return {"new_user": user}

@app.get("/listusers")
async def list_user():
    users = repo.list()
    return {"all_users": users}
