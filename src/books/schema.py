from pydantic import BaseModel


# create book validation model
class book(BaseModel):
    id: int
    name: str
    author: str

# update book validation model
class updateBook(BaseModel):
    name: str
    author: str
