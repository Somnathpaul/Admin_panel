from fastapi import APIRouter, status, Depends
from typing import Optional, List
from pydantic import BaseModel
from fastapi.exceptions import HTTPException




from src.books.schema import Book, updateBook, createBook
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




# Search a book by id
@router.get('/search/{book_id}', response_model=Book)
async def get_book_by_id(book_id:str, session: AsyncSession = Depends(get_session)):

    book = await book_service.get_books(book_id, session)

    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail= 'Book id not found')


# create a book 
@router.post("create/book/",status_code=status.HTTP_201_CREATED, response_model=Book)

async def create_a_book(book_data: createBook,
                        session: AsyncSession = Depends(get_session)) -> list:
      new_book = await book_service.create_book(book_data, session)
      return new_book


    

# update a book
@router.patch('/update/{update_id}', response_model=Book)
async def update_book(book_id:str, updateBook_data: updateBook, 
                      session: AsyncSession = Depends(get_session)) -> dict:

    updatedBook = await book_service.update_book(book_id, updateBook_data, session)

    if updateBook:
        return updatedBook
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail= f'Book id {book_id} not found')




# delete a book
@router.delete('/delete/{book_id}')
async def delete_book_by_id(book_id:str, session: AsyncSession = Depends(get_session)):

    delete_book = book_service.delete_book(book_id, session)

    if delete_book:
        return {"message": "Book deleted"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail= f'Book id {book_id} not found')