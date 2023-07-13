from fastapi import APIRouter, Depends
from config import getDB
from sqlalchemy.orm import Session
from schemas import RequestTipoExamen, Response
from crud import tipoExamenCrud as crud

router_tipo_examen = APIRouter()

# @router_genero.post('/create')
# async def create_genero(request:RequestExamen, db:Session=Depends(getDB)):
#     _estados = crud.create_genero(db, request.parameter)
#     return Response(code=200, status='ok', message='se ha creado un genero', result=_estados).dict(exclude_none=True)

@router_tipo_examen.get('/get')
async def get_tipos_examenes(db:Session=Depends(getDB)):
    _var = crud.get_tipos_examenes(db, 0, 100)
    return Response(code=200, status='ok', message='se trajo todos los estados', result=_var).dict(exclude_none=True)

@router_tipo_examen.get('/get/{id}')
async def get_tipo_examen_id(id:int, db:Session=Depends(getDB)):
    _var = crud.get_tipo_examen_id(db, id)
    return Response(code=200, status='ok', message='se trajo un estado', result=_var).dict(exclude_none=True)

# @router_genero.post('/update')
# async def update_genero(request:RequestExamen, db:Session=Depends(getDB)):
#     _estados = crud.update_genero(db, request.parameter)
#     return Response(code=200, status='ok', message='se actualizo una genero', result=_estados).dict(exclude_none=True)

# @router_genero.delete('/delete/{id}')
# async def delete_genero(id:int, db:Session=Depends(getDB)):
#     crud.delete_genero(db, id)
#     return Response(code=200, status='ok', message='se elimino un genero').dict(exclude_none=True)
