from sqlalchemy.orm import Session

from models.book import Book


def get_all_books(session: Session) -> list[Book]:
    return session.query(Book).all()


def get_book_by_id(session: Session, book_id: int) -> Book | None:
    return session.get(Book, book_id)


def create_book(session: Session, data: dict) -> Book:
    book = Book(**data)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


def delete_book(session: Session, book_id: int) -> bool:
    book = session.get(Book, book_id)
    if book is None:
        return False
    session.delete(book)
    session.commit()
    return True


def update_book(session: Session, book_id: int, data: dict) -> Book | None:
    book = session.get(Book, book_id)
    if book is None:
        return None
    for key, value in data.items():
        setattr(book, key, value)
    session.commit()
    session.refresh(book)
    return book
