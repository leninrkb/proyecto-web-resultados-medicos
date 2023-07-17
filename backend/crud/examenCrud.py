from sqlalchemy.orm import Session
from schemas import ExamenSchema
from models import Examen

def get_examenes(db:Session, skip:int=0, limit:int=100):
    return db.query(Examen).offset(skip).limit(limit).all()

def get_examen_id(db:Session, id:int):
    return db.query(Examen).filter(Examen.id == id).first()

def create_examen(db:Session, examen:ExamenSchema):
    _var = Examen(
        id_institucion = examen.id_institucion,
        id_persona = examen.id_persona,
        id_estado = examen.id_estado,
        examen = examen.examen,
        motivo = examen.motivo,
        fecha_realiza = examen.fecha_realiza,
        observacion = examen.observacion,
    )
    db.add(_var)
    db.commit()
    db.refresh(_var)
    return _var

def delete_examen(db:Session, id:int):
    _var = get_examen_id(db = db, id = id)
    db.delete(_var)
    db.commit()

# def update_genero(db:Session, genero:ExamenSchema):
#     _var = get_genero_id(db = db, id = genero.id)
#     _var.genero = genero.genero
#     db.commit()
#     db.refresh(_var)
#     return _var


