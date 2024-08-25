from fastapi import APIRouter, status, Depends
from typing import Optional, List
from pydantic import BaseModel
from fastapi.exceptions import HTTPException




from src.books.schema import book, updateBook
from src.books.data import books
from src.books.service import bookService

# session function 
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession


router = APIRouter()
book_service = bookService()






# ------------------------- Routes ----------------------------    

# Get all the books
@router.get('/all_books')
async def get_all_books(session: AsyncSession = Depends(get_session))-> list:
    books = await book_service.get_all_books(session)
    return books

# create a book
@router.post('/book')
async def create_book(book_data : book, session: AsyncSession = Depends(get_session)) -> dict:

    new_book = await book_service.create_book(book_data, session)

    # model dump convert object into dict
    # new_book = book_data.model_dump()

    # books.append(new_book)
    return new_book


# Search a book by id
@router.get('/book/{book_id}')
async def get_book_by_id(book_id:int, session: AsyncSession = Depends(get_session)) ->dict:

    book = await book_service.get_books(book_id, session)

    '''
    for book in books:
        if book['id'] == book_id:
            return book
    '''
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail= 'Book id not found')


# delete a book
@router.delete('/book/{book_id}')
async def delete_book(book_id:int, session: AsyncSession = Depends(get_session)) -> dict:

    delete_book = book_service.delete_book(book_id, session)

    if delete_book:
        return {"message": "Book deleted"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail= f'Book id {book_id} not found')
    


    '''
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {'message':'book deleted'}
        
    return {'message': f'book with id {book_id} not found'}
    '''



# update a book
@router.patch('/book/{update_id}')
async def update_book(book_id: int, updateBook_data: updateBook, 
                      session: AsyncSession = Depends(get_session)) -> dict:

    updatedBook = await book_service.update_book(book_id, updateBook_data, session)

    if updateBook:
        return updatedBook
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail= f'Book id {book_id} not found')


    '''
    for book in books:
        if book['id'] == book_id:
            book['name'] = updateBook_data.name
            book['author'] = updateBook_data.author

            return book
    '''
        
    return {'message': f'book with id {book_id} not found'}