from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace 'your_database_url' with the actual connection string to your database
# Example connection string for SQLite: 'sqlite:///example.db'
engine = create_engine('your_database_url')

Base = declarative_base()

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()