
from fastapi import FastAPI

from database import Base, engine
from routers.book import router as book_router
from models.book import Book

app = FastAPI()

Base.metadata.create_all(engine)
app.include_router(book_router)

