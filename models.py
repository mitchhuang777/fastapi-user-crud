from db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import TypeDecorator
from datetime import datetime


"""
class user_management:
id str
title str
content str
date_created datetime
"""

class Email(TypeDecorator):
    impl = str
    
    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        if '@' not in value or ".com" not in value:
            raise ValueError("Invalid email address format")

class UserManagement(Base):
    __tablename__ = 'user_management'
    id : Mapped[str] = mapped_column(primary_key=True)
    name : Mapped[str] 
    email : Mapped[str] 
    password : Mapped[str]
    createTime : Mapped[datetime] = mapped_column(default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<UserManagement {self.id} at {selft.createTime}>"
    