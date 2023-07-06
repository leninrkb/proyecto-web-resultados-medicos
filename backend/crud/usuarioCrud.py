from sqlalchemy.orm import Session
from schemas import UsuarioSchema
from models import Usuario

def get(db:Session, skip:int=0, limit:int=100):
    return db.query(Usuario).offset(skip).limit(limit).all()

def getId(db:Session, id:int):
    return db.query(Usuario).filter(Usuario.id == id).first()

def create(db:Session, usuario:UsuarioSchema):
    _usuario = Usuario(
        id_persona = usuario.id_persona,
        id_rol = usuario.id_rol,
        usuario = usuario.usuario,
        contrasena = usuario.contrasena,
    )
    db.add(_usuario)
    db.commit()
    db.refresh(_usuario)
    return _usuario

def delete(db:Session, id:int):
    _usuario = getId(db = db, id = id)
    db.delete(_usuario)
    db.commit()

def update(db:Session, usuario:UsuarioSchema):
    _usuario = getId(db = db, id = usuario.id)
    _usuario.id_rol = usuario.id_rol
    _usuario.usuario = usuario.usuario
    _usuario.contrasena = usuario.contrasena
    db.commit()
    db.refresh(_usuario)
    return _usuario


