from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.logger_config import logger

SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base= declarative_base()

def get_db():
    logger.info("Opening new database session")
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Error during DB session: {e}")
        raise
    finally:
        db.close()
        logger.info("Database session closed")
