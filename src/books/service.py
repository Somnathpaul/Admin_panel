from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc



from src.books.schema import createBook, updateBook
from src.books.models import Book




class bookService:

    async def get_all_books(self, session: AsyncSession):

        statement = select(Book).order_by(desc.created_at)

        result = await session.exec(statement)
        return result.all()
    


    async def get_books(self, book_uuid:str, session: AsyncSession):

        statement = select(Book).where(Book.uuid == book_uuid)

        result = await session.exec(statement)
        book = result.first()


        return book if book is not None else None
    


    async def create_book(self, book_data:createBook, session: AsyncSession):

        # convert the data to dict
        book_data_dict = book_data.model_dump()

        # create new book
        new_book = Book(**book_data_dict)

        # add new data to the database
        session.add(new_book)
        await session.commit()

        return new_book


    async def update_book(self, book_uuid:str, book_data: updateBook, session: AsyncSession):

        # get book data
        book_update = self.get_books(book_uuid, session)

        if book_update is not None:
            # convert the data to dict
            update_data_dict = book_data.model_dump()

            for k,v in update_data_dict.items():
                setattr(book_update, k,v)

            # commit to the database
            await session.commit()
            return book_update
        else:
            return {"Message": "Error. No book found"}

    async def delete_book(self, book_uuid: str, session: AsyncSession):
        
        # get book data
        book_delete = self.get_books(book_uuid, session)

        if book_delete is not None:
            await session.delete(book_delete)

            await session.commit()

            return {"message": "Book deleted"}

        else:
            return {"message": "Not found"}