from fastapi import APIRouter, Depends
from config import getDB
from sqlalchemy.orm import Session
from schemas import RequestUsuario, Response
from crud import usuarioCrud as crud

router_usuario = APIRouter()

@router_usuario.post('/create')
async def create_usuario(request:RequestUsuario, db:Session=Depends(getDB)):
    _usuario = crud.create(db, request.parameter)
    return Response(code=200, status='ok', message='se ha creado un usuario', result=_usuario).dict(exclude_none=True)

@router_usuario.get('/get')
async def get_usuarios(db:Session=Depends(getDB)):
    _usuarios = crud.get(db, 0, 100)
    return Response(code=200, status='ok', message='se trajo todos los usuarios', result=_usuarios).dict(exclude_none=True)

@router_usuario.get('/get/{id}')
async def get_usuario_id(id:int, db:Session=Depends(getDB)):
    _usuario = crud.getId(db, id)
    return Response(code=200, status='ok', message='se trajo un usuario', result=_usuario).dict(exclude_none=True)

@router_usuario.post('/update')
async def update_usuario(request:RequestUsuario, db:Session=Depends(getDB)):
    _usuario = crud.update(db, request.parameter)
    return Response(code=200, status='ok', message='se actualizo un usuario', result=_usuario).dict(exclude_none=True)

@router_usuario.delete('/delete/{id}')
async def delete_usuario(id:int, db:Session=Depends(getDB)):
    crud.delete(db, id)
    return Response(code=200, status='ok', message='se elimino un usuario').dict(exclude_none=True)


@router_usuario.post('/autenticar')
async def autenticar_usuario(request:RequestUsuario, db:Session=Depends(getDB)):
    _usuario = crud.autenticar(db, request.parameter)
    return Response(code=200, status='ok', message='autenticado', result=_usuario).dict(exclude_none=True)
