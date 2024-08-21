from fastapi import APIRouter, status
from typing import Optional, List
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

from src.books.schema import book, updateBook
from src.books.data import books


router = APIRouter()









@router.get('/')
async def read_root():
    return {'Message': 'Hello World'}


@router.get('/app/{name}')
async def name(name:str) -> dict:
    return {'message': f'hello {name}'}


@router.get('/app')
async def letsee(name:str) -> dict:
    return {'message': f'hello {name}'}

@router.get('/web/{name}')
async def mix(name:str, age:int) -> dict:
    return {'message': f'hello {name}', 'age': age}

@router.get('/secure')
async def secure(name:Optional[str] = 'None', location: str = 'None', number:int = 0) -> dict:
    return {'name': name, 'location': location, 'number' : number}



class UserSchemas_create_account(BaseModel):
    name: str
    email: str
    password: str


@router.post('/create_account')
async def create_account(user_data : UserSchemas_create_account ) -> dict:
    new_user = {
        'name': user_data.name,
        'email': user_data.email,
        'password': user_data.password
    }
    return new_user







# ------------------------- Routes ----------------------------    

# Get all the books
@router.get('/all_books')
async def get_all_books()-> list:
    return books

# create a book
@router.post('/book')
async def create_book(book_data : book) -> dict:
    new_book = book_data.model_dump() # model dump convert object into dict

    books.append(new_book)
    return new_book


# Search a book by id
@router.get('/book/{book_id}')
async def get_book_by_id(book_id:int) ->dict:
    for book in books:
        if book['id'] == book_id:
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail= 'Book id not found')


# delete a book
@router.delete('/book/{book_id}')
async def delete_book(book_id:int) -> dict:
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {'message':'book deleted'}
        
    return {'message': f'book with id {book_id} not found'}
# update a book

@router.patch('/book/{update_id}')
async def update_book(book_id: int, updateBook_data: updateBook) -> dict:

    for book in books:
        if book['id'] == book_id:
            book['name'] = updateBook_data.name
            book['author'] = updateBook_data.author

            return book
        
    return {'message': f'book with id {book_id} not found'}