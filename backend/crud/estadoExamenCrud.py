from sqlalchemy.orm import Session
from schemas import EstadoExamenSchema
from models import EstadoExamen

def get_estados_examenes(db:Session, skip:int=0, limit:int=100):
    return db.query(EstadoExamen).offset(skip).limit(limit).all()

def get_estado_examen_id(db:Session, id:int):
    return db.query(EstadoExamen).filter(EstadoExamen.id == id).first()

# def create_genero(db:Session, genero:ExamenSchema):
#     _genero = Examen(
#         genero = genero.genero
#     )
#     db.add(_genero)
#     db.commit()
#     db.refresh(_genero)
#     return _genero

# def delete_genero(db:Session, id:int):
#     _genero = get_genero_id(db = db, id = id)
#     db.delete(_genero)
#     db.commit()

# def update_genero(db:Session, genero:ExamenSchema):
#     _genero = get_genero_id(db = db, id = genero.id)
#     _genero.genero = genero.genero
#     db.commit()
#     db.refresh(_genero)
#     return _genero


