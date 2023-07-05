from fastapi import APIRouter, Depends
from config import getDB
from sqlalchemy.orm import Session
from schemas import RequestRolUsuario, Response
from crud import rolUsuarioCrud as crud

router_rol_usuario = APIRouter()

@router_rol_usuario.post('/create')
async def create_rol_usuario(request:RequestRolUsuario, db:Session=Depends(getDB)):
    _rol_usuario = crud.create_rol_usuario(db, request.parameter)
    return Response(code=200, status='ok', message='se ha creado un rol', result=_rol_usuario).dict(exclude_none=True)

@router_rol_usuario.get('/get')
async def get_roles_usuarios(db:Session=Depends(getDB)):
    _roles_usuario = crud.get_roles_usuarios(db, 0, 100)
    return Response(code=200, status='ok', message='se trajo todos los roles', result=_roles_usuario).dict(exclude_none=True)

@router_rol_usuario.get('/get/{id}')
async def get_rol_usuario_id(id:int, db:Session=Depends(getDB)):
    _rol_usuario = crud.get_rol_usuario_id(db, id)
    return Response(code=200, status='ok', message='se trajo un rol', result=_rol_usuario).dict(exclude_none=True)

@router_rol_usuario.post('/update')
async def update_rol_usuario(request:RequestRolUsuario, db:Session=Depends(getDB)):
    _rol_usuario = crud.update_rol_usuario(db, request.parameter)
    return Response(code=200, status='ok', message='se actualizo un rol', result=_rol_usuario).dict(exclude_none=True)

@router_rol_usuario.delete('/delete/{id}')
async def delete_rol_usuario(id:int, db:Session=Depends(getDB)):
    crud.delete_rol_usuario(db, id)
    return Response(code=200, status='ok', message='se elimino un rol').dict(exclude_none=True)
