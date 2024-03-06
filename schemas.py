from pydantic import BaseModel, ConfigDict
from datetime import datetime

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
    email : str
    password : str
    
    model_config = ConfigDict(
        from_attributes = True,
        json_schema_extra={
            "example":{
                "name": "SampleUserName",
                "password": "password",
                "email": "xxx@.com"
            }
        }
    )