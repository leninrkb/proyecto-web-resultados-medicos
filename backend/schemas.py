from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from datetime import date

T = TypeVar('T')

class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

########## persona
class PersonaSchema(BaseModel):
    id: int
    cedula: str
    nombres: str
    apellidos: str
    fecha_nacimiento: date
    id_genero: int
    class Config:
        orm_mode = True
class RequestGenero(BaseModel):
    parameter: PersonaSchema = Field(...)


########## genero
class GeneroSchema(BaseModel):
    id: int
    genero: str
    class Config:
        orm_mode = True
class RequestGenero(BaseModel):
    parameter: GeneroSchema = Field(...)


########## rol de usuario
class RolUsuarioSchema(BaseModel):
    id: int
    rol: str
    descripcion: str
    class Config:
        orm_mode = True
class RequestRolUsuario(BaseModel):
    parameter: RolUsuarioSchema = Field(...)

