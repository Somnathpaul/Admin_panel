from sqlmodel import SQLModel, Field, Column
from datetime import date

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
    #published_date: date
    #updated_date: date


    def __repr__(self):
        return f"<book {self.title}>"
    