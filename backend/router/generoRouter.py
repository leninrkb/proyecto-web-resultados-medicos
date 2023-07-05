from fastapi import APIRouter, Depends
from config import getDB
from sqlalchemy.orm import Session
from schemas import RequestGenero, Response
from crud import generoCrud as crud

router_genero = APIRouter()

@router_genero.post('/create')
async def create_genero(request:RequestGenero, db:Session=Depends(getDB)):
    _genero = crud.create_genero(db, request.parameter)
    return Response(code=200, status='ok', message='se ha creado un genero', result=_genero).dict(exclude_none=True)

@router_genero.get('/get')
async def get_generos(db:Session=Depends(getDB)):
    _generos = crud.get_generos(db, 0, 100)
    return Response(code=200, status='ok', message='se trajo todas los generos', result=_generos).dict(exclude_none=True)

@router_genero.get('/get/{id}')
async def get_genero_id(id:int, db:Session=Depends(getDB)):
    _genero = crud.get_genero_id(db, id)
    return Response(code=200, status='ok', message='se trajo una genero', result=_genero).dict(exclude_none=True)

@router_genero.post('/update')
async def update_genero(request:RequestGenero, db:Session=Depends(getDB)):
    _genero = crud.update_genero(db, request.parameter)
    return Response(code=200, status='ok', message='se actualizo una genero', result=_genero).dict(exclude_none=True)

@router_genero.delete('/delete/{id}')
async def delete_genero(id:int, db:Session=Depends(getDB)):
    crud.delete_genero(db, id)
    return Response(code=200, status='ok', message='se elimino un genero').dict(exclude_none=True)
