from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/elopark"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

BASE = declarative_base()


async def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()