from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import DATABASE_URL

def connect_db(db_url):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    session = Session(bind=engine)
    try:
        yield session
    finally:
        session.close()