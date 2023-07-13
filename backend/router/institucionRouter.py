from fastapi import APIRouter, Depends
from config import getDB
from sqlalchemy.orm import Session
from schemas import RequestInstitucion, Response
from crud import institucionCrud as crud

router_institucion = APIRouter()

# @router_genero.post('/create')
# async def create_genero(request:RequestExamen, db:Session=Depends(getDB)):
#     _var = crud.create_genero(db, request.parameter)
#     return Response(code=200, status='ok', message='se ha creado un genero', result=_var).dict(exclude_none=True)

@router_institucion.get('/get')
async def get_instituciones(db:Session=Depends(getDB)):
    _var = crud.get_instituciones(db, 0, 100)
    return Response(code=200, status='ok', message='se trajo todo', result=_var).dict(exclude_none=True)

@router_institucion.get('/get/{id}')
async def get_institucion_id(id:int, db:Session=Depends(getDB)):
    _var = crud.get_institucion_id(db, id)
    return Response(code=200, status='ok', message='se trajo uno', result=_var).dict(exclude_none=True)

# @router_genero.post('/update')
# async def update_genero(request:RequestExamen, db:Session=Depends(getDB)):
#     _var = crud.update_genero(db, request.parameter)
#     return Response(code=200, status='ok', message='se actualizo una genero', result=_var).dict(exclude_none=True)

# @router_genero.delete('/delete/{id}')
# async def delete_genero(id:int, db:Session=Depends(getDB)):
#     crud.delete_genero(db, id)
#     return Response(code=200, status='ok', message='se elimino un genero').dict(exclude_none=True)
