from sqlalchemy.orm import Session
from schemas import BookUpdate, BookCreate
from models import BookModel

def get_book(db: Session, book_id: int):
    """
    function that takes an ID and returns only that ID
    """
    return db.query(BookModel).filter(BookModel.id == book_id).first()

def get_books(db: Session):
    """
    function that returns all records
    """
    return db.query(BookModel).all()

def create_book(db: Session, book: BookCreate):
    """
    function that creates a new record
    """
    db_book = BookModel(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book: BookUpdate, book_id: int):
    """
    function that updates the values for an existing record
    """
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if db_book is None:
        return None

    if db_book.author is not None:
        db_book.author = book.author
    if db_book.description is not None:
        db_book.description = book.description
    if db_book.genre is not None:
        db_book.genre = book.genre
    if db_book.is_avaiable is not None:
        db_book.is_avaiable = book.is_avaiable
    if db_book.page_count is not None:
        db_book.page_count = book.page_count
    if db_book.publisher is not None:
        db_book.publisher = book.publisher
    if db_book.publication_year is not None:
        db_book.publication_year = book.publication_year
    if db_book.title is not None:
        db_book.title = book.title
    
    db.commit()
    return db_book

def delete_book(db: Session, book_id: int):
    """
    function that deletes an existing record
    """
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    db.delete(db_book)
    db.commit()
    return db_book
