from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal, get_db
from schemas import BookUpdate, BookCreate, BookResponse
from typing import List
from controllers import (
    create_book,
    update_book,
    get_book,
    get_books,
    delete_book
)

router = APIRouter()


@router.get("/books/{book_id}", response_model = BookResponse)
def get_book_router(book_id: int, db:Session = Depends(get_db)):
    db_book = get_book(db = db, book_id = book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail = "Book not found")    
    return db_book


@router.get("/books/", response_model = list[BookResponse])
def get_books_router(db:Session = Depends(get_db)):
    return get_books(db = db)


@router.post("/books/", response_model = BookResponse)
def create_book_router(book: BookCreate, db:Session = Depends(get_db)):
    return create_book(db = db, book = book)


@router.put("/books/{book_id}", response_model = BookResponse)
def update_book_router(book: BookUpdate, book_id: int, db:Session = Depends(get_db)):
    db_book = update_book(db = db, book = book, book_id = book_id)
    if db_book is None:
        raise HTTPException(status_code = 404, detail = "Book not found")
    return db_book

@router.delete("/books/{book_id}", response_model = BookResponse)
def delete_book_router(book_id: int, db:Session = Depends(get_db)):
    db_book = delete_book(db = db, book_id = book_id)
    if db_book is None:
        raise HTTPException(status_code = 404, detail = "Book not found")
    return db_book


