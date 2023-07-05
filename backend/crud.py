from sqlalchemy.orm import Session
from schemas import PersonaSchema
from models import PersonaModel

def getPersonas(db:Session, skip:int=0, limit:int=100):
    return db.query(PersonaModel).offset(skip).limit(limit).all()

def getPersonaId(db:Session, id:int):
    return db.query(PersonaModel).filter(PersonaModel.id == id).first()

def createPersona(db:Session, persona:PersonaSchema):
    _persona = PersonaModel(
        cedula = persona.cedula,
        nombres = persona.nombres,
        apellidos = persona.apellidos,
        fecha_nacimiento = persona.fecha_nacimiento,
        id_genero = persona.id_genero
    )
    db.add(_persona)
    db.commit()
    db.refresh(_persona)
    return _persona

def deletePersona(db:Session, id:int):
    _persona = getPersonaId(db = db, id = id)
    db.delete(_persona)
    db.commit()

def updatePersona(db:Session, persona:PersonaSchema):
    _persona = getPersonaId(db = db, id = persona.id)
    _persona.cedula = persona.cedula
    _persona.nombres = persona.nombres
    _persona.apellidos = persona.apellidos
    _persona.fecha_nacimiento = persona.fecha_nacimiento
    _persona.id_genero = persona.id_genero
    db.commit()
    db.refresh(_persona)
    return _persona


