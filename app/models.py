from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.db import Base

class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, index = True)
    author = Column(String, index = True)
    publication_year = Column(Integer, index =True, nullable = True)
    genre = Column(String, index = True, nullable = True)
    publisher = Column(String, index = True, nullable = True)
    page_count = Column(String, index = True, nullable = True)
    description = Column(String, index = True, nullable = True)
    is_available = Column(Boolean, index = True)
    created_at = Column(DateTime, default = func.now(), index = True)