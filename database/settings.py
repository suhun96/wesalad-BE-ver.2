import os

from dotenv                     import load_dotenv
from sqlalchemy                 import create_engine
from sqlalchemy.orm             import sessionmaker, registry
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST     = os.getenv("DB_HOST")
DB_PORT     = os.getenv("DB_PORT")
DB_DATABASE = os.getenv("DB_DATABASE")

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

Base = declarative_base()
mapper_registry = registry()

Engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)


def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

mapper_registry.configure()