from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BookBase(BaseModel):
    title: str
    author: str
    publication_year: Optional[int] = None
    genre: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    description: Optional[str] = None
    is_avaiable: bool

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int
    created_at = datetime

    class Config:
        orm_mode = True

class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None
    publication_year: Optional[int] = None
    genre: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    description: Optional[str] = None
    is_avaiable: Optional[bool] = None
