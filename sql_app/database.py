from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
pg_username = os.getenv("PG_USERNAME", "DEFAULT")
pg_password = os.getenv("PG_PASSWORD", "Secret")
host = os.getenv("PG_HOST","DEFAULT")
db_name = os.getenv("PG_DB","DEFAULT")
db_string = f"postgresql://{pg_username}:{pg_password}@{host}:5432/{db_name}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
