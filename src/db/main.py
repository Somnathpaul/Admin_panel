
from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import config

# create an engine
engine = AsyncEngine(
    create_engine(
    url=config.DATABASE_URL,
    echo=True
))


# create a connection to the database
async def init_db():
    async with engine.begin() as conn:
        statement = text("SELECT 'hello';")

        result = await conn.execute(statement)
        
        print(result.all())