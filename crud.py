from models import UserManagement
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select

class CRUD:
    async def get_all(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            statement = select(UserManagement).order_by(UserManagement.id)
            
            result = await session.execute(statement)
            
            return result.scalars()
    
    async def add(self, async_session: async_sessionmaker[AsyncSession], usermanagement: UserManagement):
        async with async_session() as session:
            session.add(usermanagement)
            await session.commit()
            
            return usermanagement
            
    async def get_by_id(self, async_session: async_sessionmaker[AsyncSession], usermanagement_id: str):
        async with async_session() as session:
            statement = select(UserManagement).filter(UserManagement.id == usermanagement_id)
            result = await session.execute(statement)
            return result.scalars().one()
            
    async def update(self, async_session: async_sessionmaker[AsyncSession], usermanagement_id: str, data):
        async with async_session() as session:
            statement = select(UserManagement).filter(UserManagement.id == usermanagement_id)
            result = await session.execute(statement)
            usermanagement = result.scalars().one()
            
            usermanagement.email = data['email']
            usermanagement.password = data['password']
            usermanagement.name = data['name']
            
            await session.commit()
            
            return usermanagement
        
    async def delete(self, async_session: async_sessionmaker[AsyncSession], usermanagement: UserManagement):
        async with async_session() as session:
            await session.delete(usermanagement)
            await session.commit()
            