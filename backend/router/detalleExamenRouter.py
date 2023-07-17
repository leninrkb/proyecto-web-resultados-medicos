from fastapi import APIRouter, Depends
from config import getDB
from sqlalchemy.orm import Session
from schemas import RequestDetalleExamen, Response
from crud import detalleExamenCrud as crud

router_detalle = APIRouter()

@router_detalle.post('/create')
async def create_genero(request:RequestDetalleExamen, db:Session=Depends(getDB)):
    _var = crud.create_detalle(db, request.parameter)
    return Response(code=200, status='ok', message='se ha creado un detalle', result=_var).dict(exclude_none=True)

@router_detalle.get('/get')
async def get_detalles(db:Session=Depends(getDB)):
    _var = crud.get_detalles(db, 0, 100)
    return Response(code=200, status='ok', message='se trajo todo', result=_var).dict(exclude_none=True)

@router_detalle.get('/get/{id}')
async def get_detalle_id(id:int, db:Session=Depends(getDB)):
    _var = crud.get_detalles_id(db, id)
    return Response(code=200, status='ok', message='se trajo uno', result=_var).dict(exclude_none=True)

# @router_genero.post('/update')
# async def update_genero(request:RequestExamen, db:Session=Depends(getDB)):
#     _var = crud.update_genero(db, request.parameter)
#     return Response(code=200, status='ok', message='se actualizo una genero', result=_var).dict(exclude_none=True)

# @router_genero.delete('/delete/{id}')
# async def delete_genero(id:int, db:Session=Depends(getDB)):
#     crud.delete_genero(db, id)
#     return Response(code=200, status='ok', message='se elimino un genero').dict(exclude_none=True)
