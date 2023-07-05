from sqlalchemy import DATE, Column, Integer, String
from config import Base, engine

class PersonaModel(Base):
    __tablename__ = 'persona'
    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String)
    nombres = Column(String)
    apellidos = Column(String)
    fecha_nacimiento = Column(DATE)
    id_genero = Column(Integer)

Base.metadata.create_all(engine)