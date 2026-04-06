from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas.books import BookResponse, BookCreate
from services.book_service import (get_all_books,
                                   create_book, get_book_by_id,
                                   delete_book, update_book)

router = APIRouter(prefix="/books", tags=["books"])


def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@router.get("", response_model=list[BookResponse])
def get_books(session: Session = Depends(get_session)) -> list[BookResponse]:
    return get_all_books(session)


@router.post("", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create(data: BookCreate, session: Session = Depends(get_session)) -> BookResponse:
    return create_book(session, data.model_dump())


@router.get("/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def get_book(book_id: int, session: Session = Depends(get_session)) -> BookResponse:
    book = get_book_by_id(session, book_id)

    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(book_id: int, session: Session = Depends(get_session)) -> None:
    ok = delete_book(session, book_id)
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@router.put("/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def update(book_id: int, data: BookCreate, session: Session = Depends(get_session)) -> BookResponse:
    book = update_book(session, book_id, data.model_dump())

    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book
