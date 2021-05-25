import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('MARIADB_DATABASE')
DB_USER = os.environ.get('MARIADB_USER')
DB_PASS = os.environ.get('MARIADB_PASSWORD')

DATABASE_URL = f"mariadb+mariadbconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
