from pydantic import BaseModel, ConfigDict, field_validator
from pydantic import constr, EmailStr, Field
from datetime import datetime
from typing import Optional

class UserManagementModel(BaseModel):
    id : str
    name : str
    email : str
    password : str
    createTime : datetime
    
    model_config = ConfigDict(
        from_attributes = True
    )
    
class UserCreateModel(BaseModel):
    name : str
    email : EmailStr()
    password: str
    
    @field_validator('name')
    @classmethod
    def name_must_contain_space(cls, v:str):
        if ' ' not in v:
            raise ValueError('Owner name must contain a space')
        return v
    
    @field_validator('password')
    @classmethod
    def password_validation(cls, v: str, email: str):
        # Check password whether longer than 8 characters.
        if len(v) < 4:
            raise ValueError('Password length should be at least 8 characters')
        # Check password contains at least one digit.
        if not any(char.isdigit() for char in v):
            raise ValueError('Password should contain at least one digit')
        # Check password contains at least one uppercase letter.
        if not any(char.isupper() for char in v):
            raise ValueError('Password should contain at least one uppercase letter')
       # Check password contains at least one lowercase letter.
        if not any(char.islower() for char in v):
            raise ValueError('Password should contain at least one lowercase letter')
        return v
    
    model_config = ConfigDict(
        from_attributes = True,
        json_schema_extra={
            "example":{
                "name": "Bill Gates",
                "password": "Th1sA3eCREtP3D#",
                "email": "helloworld@gmail.com"
            }
        }
    )