from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

if "TEST_DATABASE_URL" in os.environ:
    DATABASE_URL = os.environ.get("TEST_DATABASE_URL")
else:
    DATABASE_URL ='postgresql://tmc:tmc@db:5432/tmc'
db_engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
Base = declarative_base()
