from sqlalchemy.orm import Session
from schemas import GeneroSchema
from models import Genero

def get_generos(db:Session, skip:int=0, limit:int=100):
    return db.query(Genero).offset(skip).limit(limit).all()

def get_genero_id(db:Session, id:int):
    return db.query(Genero).filter(Genero.id == id).first()

def create_genero(db:Session, genero:GeneroSchema):
    _genero = Genero(
        genero = genero.genero
    )
    db.add(_genero)
    db.commit()
    db.refresh(_genero)
    return _genero

def delete_genero(db:Session, id:int):
    _genero = get_genero_id(db = db, id = id)
    db.delete(_genero)
    db.commit()

def update_genero(db:Session, genero:GeneroSchema):
    _genero = get_genero_id(db = db, id = genero.id)
    _genero.genero = genero.genero
    db.commit()
    db.refresh(_genero)
    return _genero


