from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'postgresql+psycopg2://user_postgre:FeBjjTD0iNohhn66Zp2VEQYHN6wrNGsU@dpg-cihmmh5gkuvojja3p9lg-a.oregon-postgres.render.com/examenes'
engine = create_engine(DATABASE_URL)
# session_local = sessionmaker(autoflush=False, bind=engine)
SessionLocal  = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()