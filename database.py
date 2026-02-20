
# import os
# from dotenv import load_dotenv
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")

# # SQLite needs connect_args, MySQL doesn't
# connect_args = {"check_same_thread": False} if DATABASE_URL and DATABASE_URL.startswith("sqlite") else {}

# engine = create_engine(DATABASE_URL, connect_args=connect_args)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# import os
# from dotenv import load_dotenv
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")

# # SQLite needs connect_args, MySQL doesn't
# connect_args = {"check_same_thread": False} if DATABASE_URL and DATABASE_URL.startswith("sqlite") else {}

# engine = create_engine(DATABASE_URL, connect_args=connect_args)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///shortener.db")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()