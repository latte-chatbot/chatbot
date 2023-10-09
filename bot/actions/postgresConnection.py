import os
from sqlalchemy import create_engine, Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


PG_DB = os.environ['PG_DB']
PG_USERNAME = os.environ['PG_USERNAME']
PG_PASSWORD = os.environ['PG_PASSWORD']


Base = declarative_base()


class UserInfo(Base):
    __tablename__ = "usuario_info"
    id = Column(String, primary_key=True)


print("[INFO] Connecting to Postgres...")
DATABASE_URL = f"postgresql+psycopg2://{PG_USERNAME}:{PG_PASSWORD}@postgres:5432/{PG_DB}"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)
print("[INFO] Connected to Postgres!")
