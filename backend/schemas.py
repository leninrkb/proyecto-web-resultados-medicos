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
class RequestPersona(BaseModel):
    parameter: PersonaSchema = Field(...)


########## genero
class GeneroSchema(BaseModel):
    id: int
    genero: str
    class Config:
        orm_mode = True
class RequestExamen(BaseModel):
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


########## usuario
class UsuarioSchema(BaseModel):
    id: int
    id_persona: int
    id_rol: int
    usuario: str
    contrasena: str
    class Config:
        orm_mode = True
class RequestUsuario(BaseModel):
    parameter: UsuarioSchema = Field(...)


########## examen
class ExamenSchema(BaseModel):
    id : int
    id_institucion : int
    id_persona : int
    id_estado : int
    examen : str
    motivo: str
    fecha_realiza : date
    observacion : str
    class Config:
        orm_mode = True
class RequestExamen(BaseModel):
    parameter: ExamenSchema = Field(...)


########## estado examen
class EstadoExamenSchema(BaseModel):
    id : int
    estado : str
    descripcion : str
    class Config:
        orm_mode = True
class RequestEstadoExamen(BaseModel):
    parameter: EstadoExamenSchema = Field(...)


########## tipo examen
class TipoExamenSchema(BaseModel):
    id : int
    tipo : str
    referencia : str
    descripcion : str
    precio : float
    class Config:
        orm_mode = True
class RequestTipoExamen(BaseModel):
    parameter: TipoExamenSchema = Field(...)


########## institucion
class InstitucionSchema(BaseModel):
    id : int
    institucion : str
    razon_social : str
    descripcion : str
    ubicacion : str
    path_img : str
    class Config:
        orm_mode = True
class RequestInstitucion(BaseModel):
    parameter: InstitucionSchema = Field(...)

