from sqlalchemy.orm import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://itr:itr123@localhost:5432/itr')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    try:
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        SessionLocal().commit()
        print("Tables created successfully!")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    create_tables()
