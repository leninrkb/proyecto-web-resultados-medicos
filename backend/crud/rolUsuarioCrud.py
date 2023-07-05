from sqlalchemy.orm import Session
from schemas import RolUsuarioSchema
from models import RolUsuario

def get_roles_usuarios(db:Session, skip:int=0, limit:int=100):
    return db.query(RolUsuario).offset(skip).limit(limit).all()

def get_rol_usuario_id(db:Session, id:int):
    return db.query(RolUsuario).filter(RolUsuario.id == id).first()

def create_rol_usuario(db:Session, rol:RolUsuarioSchema):
    _rol_usuario = RolUsuario(
        rol = rol.rol,
        descripcion = rol.descripcion,
    )
    db.add(_rol_usuario)
    db.commit()
    db.refresh(_rol_usuario)
    return _rol_usuario

def delete_rol_usuario(db:Session, id:int):
    _rol_usuario = get_rol_usuario_id(db = db, id = id)
    db.delete(_rol_usuario)
    db.commit()

def update_rol_usuario(db:Session, rol:RolUsuarioSchema):
    _rol_usuario = get_rol_usuario_id(db = db, id = rol.id)
    _rol_usuario.rol = rol.rol
    _rol_usuario.descripcion = rol.descripcion
    db.commit()
    db.refresh(_rol_usuario)
    return _rol_usuario


