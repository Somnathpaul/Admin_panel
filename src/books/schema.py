from pydantic import BaseModel
from datetime import datetime
import uuid

# create book validation model
class book(BaseModel):
    id: uuid.UUID
    name: str
    author: str
    created_at: datetime
    updated_at: datetime


# create a book 
class createBook(BaseModel):
    name: str
    author: str
    created_at: datetime
    updated_at: datetime

# update book
class updateBook(BaseModel):
    name: str
    author: str
    created_at: datetime
    updated_at: datetime

