from sqlalchemy.orm import Session
from app.schemas import BookUpdate, BookCreate
from app.models import BookModel
from app.logger_config import logger

def get_book(db: Session, book_id: int):
    """
    function that takes an ID and returns only that ID
    """
    logger.info(f"Retrieving book details for ID={book_id}")
    return db.query(BookModel).filter(BookModel.id == book_id).first()

def get_books(db: Session):
    """
    function that returns all records
    """
    logger.info("Retrieving book details for all books")
    return db.query(BookModel).all()

def create_book(db: Session, book: BookCreate):
    """
    function that creates a new record
    """
    logger.info(f"Creating a new book record.")   
    db_book = BookModel(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book: BookUpdate, book_id: int):
    """
    function that updates the values for an existing record
    """
    logger.info(f"Updating values for book with ID: {book_id}.")  
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if db_book is None:
        return None

    if book.author is not None:
        db_book.author = book.author
    if book.description is not None:
        db_book.description = book.description
    if book.genre is not None:
        db_book.genre = book.genre
    if book.is_available is not None:
        db_book.is_available = book.is_available
    if book.page_count is not None:
        db_book.page_count = book.page_count
    if book.publisher is not None:
        db_book.publisher = book.publisher
    if book.publication_year is not None:
        db_book.publication_year = book.publication_year
    if book.title is not None:
        db_book.title = book.title
    
    db.commit()
    return db_book

def delete_book(db: Session, book_id: int):
    """
    function that deletes an existing record
    """
    logger.info(f"Deleting book with ID: {book_id}.")  
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        return None
    db.delete(db_book)
    db.commit()
    return db_book
