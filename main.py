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
    title="CRUD API", description="This is a CRUD API service.", docs_url="/"
)

session = async_sessionmaker(
    bind = engine,
    expire_on_commit=False
)
db = CRUD()

@app.get("/usermanagement", response_model=List[UserManagementModel])
async def get_all_user():
    usermanagement = await db.get_all(session)
    return usermanagement

@app.post("/usermanagement", status_code=HTTPStatus.CREATED)
async def create_user(user_data : UserCreateModel):
    new_user = UserManagement(
        id = str(uuid.uuid4()),
        name = user_data.name,
        email = user_data.email,
        password = user_data.password
    )
    
    usermanagement = await db.add(session, new_user)
    
    return usermanagement

@app.get('/usermanagement/{usermanagement_id}')
async def get_user_by_id(usermanagement_id):
    usermanagement = await db.get_by_id(session, usermanagement_id)
    return usermanagement

@app.patch("/usermanagement/{usermanagement_id}")
async def update_user(usermanagement_id: str, data: UserCreateModel):
    update_data = {}

    # Get UserCreateModel's all attribute name
    fields = data.dict().keys()

    # Add the non-null attribute into update_data dictionary
    for field in fields:
        value = getattr(data, field)
        if value is not None:
            update_data[field] = value

    # If not update any data, show the error message
    if not update_data:
        return {"error": "No fields provided for update"}, 400

    # Update the data
    usermanagement = await db.update(session, usermanagement_id, data=update_data)
    
    return usermanagement

@app.delete('/usermanagement/{usermanagement_id}', status_code=HTTPStatus.NO_CONTENT)
async def delete_user(usermanagement_id):
    usermanagement = await db.get_by_id(session, usermanagement_id)
    result = await db.delete(session, usermanagement)
    
    return result