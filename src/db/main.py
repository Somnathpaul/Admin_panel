
from sqlmodel import create_engine, SQLModel
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
       from src.books.models import Book

       await conn.run_sync(SQLModel.metadata.create_all)