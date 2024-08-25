from sqlmodel import SQLModel, Field, Column
from datetime import datetime

import uuid
import sqlalchemy.dialects.postgresql as pg


class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: uuid.UUID = Field( sa_column=Column( pg.UUID, nullable=False,
                      primary_key=True,
                      default=uuid.uuid4
                      )
                      )
    name: str
    author: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))


    def __repr__(self):
        return f"<book {self.title}>"
    