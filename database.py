import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"].replace('postgres://', 'postgresql://')
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = { "check_same_thread": False })

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 