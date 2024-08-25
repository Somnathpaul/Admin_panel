from fastapi import FastAPI

# helps to run a part of the app when needed
from contextlib import asynccontextmanager 
from src.db.main import init_db



from src.books.routes import router


@asynccontextmanager
async def life_span(app:FastAPI):
    print(f'server is starting.....')
    await init_db()
    yield
    print(f'server has been stopped')


# ---------------------------------
version = "v1"

title = "demo fastapi"
description = """
A REST API for a book review web service.

This REST API is able to;
- Create Read Update And delete books
- Add reviews to books
- Add tags to Books e.t.c.
    """
 
version_prefix ="/api/{version}"


app = FastAPI(
    title=title,
    description=description,
    version=version,
    license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
    contact={
        "name": "Ssali Jonathan",
        "url": "https://github.com/jod35",
        "email": "ssalijonathank@gmail.com",
    },
    terms_of_service="httpS://example.com/tos",
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc",
    lifespan= life_span
)



app.include_router(router, prefix=f"{version_prefix}/books", tags=["books"])