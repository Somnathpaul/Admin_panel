from pydantic import BaseModel
from datetime import date
import uuid

# create book validation model
class book(BaseModel):
    id: uuid.UUID
    name: str
    author: str
    published_date: date
    #updated_date: date


# create a book 
class createBook(BaseModel):
    name: str
    author: str
    published_date: str
    #updated_date: str
    

# update book
class updateBook(BaseModel):
    name: str
    author: str
    #updated_date: str

