from sqlalchemy import DATE, Column, Integer, String
from config import Base, engine

Base.metadata.create_all(engine)

class Persona(Base):
    __tablename__ = 'persona'
    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String)
    nombres = Column(String)
    apellidos = Column(String)
    fecha_nacimiento = Column(DATE)
    id_genero = Column(Integer)

class Genero(Base):
    __tablename__ = 'genero'
    id = Column(Integer, primary_key=True, index=True)
    genero = Column(String)

class RolUsuario(Base):
    __tablename__ = 'rol_usuario'
    id = Column(Integer, primary_key=True, index=True)
    rol = Column(String)
    descripcion = Column(String)