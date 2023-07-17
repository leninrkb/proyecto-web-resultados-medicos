from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'postgresql+psycopg2://user_postgre:elAOXyrJwpjoz04BOaiIgkMfR1qBVcdQ@dpg-cipghnt9aq0dcpq74iu0-a.oregon-postgres.render.com/examenes_9qym'
engine = create_engine(DATABASE_URL)
SessionLocal  = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
Base = declarative_base()

def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()