from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker
from crud import CRUD
from db import engine
from schemas import UserManagementModel, UserCreateModel
from http import HTTPStatus
from typing import List
from models import UserManagement
import uuid

app = FastAPI(
    title="Noted API", description="This is a simple note taking service", docs_url="/"
)

session = async_sessionmaker(
    bind = engine,
    expire_on_commit=False
)
db = CRUD()

@app.get("/usermangement", response_model=List[UserManagementModel])
async def get_all_user():
    usermanagement = await db.get_all(session)
    
    return usermanagement

@app.post("/usermangement", status_code=HTTPStatus.CREATED)
async def create_user(user_data : UserCreateModel):
    new_user = UserManagement(
        id = str(uuid.uuid4()),
        name = user_data.name,
        email = user_data.email,
        password = user_data.password
    )
    
    usermanagement = await db.add(session, new_user)
    
    return usermanagement

@app.get('/usermangement/{usermanagement_id}')
async def get_user_by_id(usermanagement_id):
    usermanagement = await db.get_by_id(session, usermanagement_id)
    return usermanagement

@app.patch("/usermangement/{usermanagement_id}")
async def update_user(usermanagement_id: str, data: UserCreateModel):
    usermanagement = await db.update(session, usermanagement_id, data={
        'name': data.name,
        'email': data.email,
        'password': data.password
    })
    return usermanagement

@app.delete('/usermanagement/{usermanagement_id}', status_code=HTTPStatus.NO_CONTENT)
async def delete_user(usermanagement_id):
    usermanagement = await db.get_by_id(session, usermanagement_id)
    result = await db.delete(session, usermanagement)
    
    return result