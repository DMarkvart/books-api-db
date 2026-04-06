from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.session import sessionmaker

DATABASE_URL = "sqlite:///books.db"

engine = create_engine(DATABASE_URL,
                       connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

