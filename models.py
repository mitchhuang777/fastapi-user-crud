from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import registry
from sqlalchemy import String, Integer, Numeric, Column
from sqlalchemy.types import TypeDecorator
from datetime import datetime

class Base(DeclarativeBase):
    pass

class UserManagement(Base):
    __tablename__ = 'user_management'
    id : Mapped[str] = mapped_column(primary_key=True)
    name : Mapped[str] 
    email : Mapped[str] 
    password : Mapped[str] 
    createTime : Mapped[datetime] = mapped_column(default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<UserManagement {self.id} at {selft.createTime}>"
    