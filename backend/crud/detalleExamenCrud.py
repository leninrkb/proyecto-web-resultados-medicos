from sqlalchemy.orm import Session
from schemas import DetalleExamenSchema
from models import DetalleExamen

def get_detalles(db:Session, skip:int=0, limit:int=100):
    return db.query(DetalleExamen).offset(skip).limit(limit).all()

def get_detalles_id(db:Session, id:int):
    return db.query(DetalleExamen).filter(DetalleExamen.id == id).first()

def create_detalle(db:Session, detalle:DetalleExamenSchema):
    _var = DetalleExamen(
        id_examen = detalle.id_examen,
        id_tipo = detalle.id_tipo,
        id_estado = detalle.id_estado,
        resultado = detalle.resultado,
        observacion = detalle.observacion,
    )
    db.add(_var)
    db.commit()
    db.refresh(_var)
    return _var

# def delete_genero(db:Session, id:int):
#     _var = get_genero_id(db = db, id = id)
#     db.delete(_var)
#     db.commit()

# def update_genero(db:Session, genero:ExamenSchema):
#     _var = get_genero_id(db = db, id = genero.id)
#     _var.genero = genero.genero
#     db.commit()
#     db.refresh(_var)
#     return _var


