
from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker


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



# db session for CRUD
async def get_session()-> AsyncSession:

    Session = sessionmaker(
        bind=engine,
        class_= AsyncSession,
        expire_on_commit= False
    )


    async with Session() as session:
        yield session