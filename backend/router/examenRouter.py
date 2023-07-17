from fastapi import APIRouter, Depends
from config import getDB
from sqlalchemy.orm import Session
from schemas import RequestExamen, Response
from crud import examenCrud as crud

router_examen = APIRouter()

@router_examen.post('/create')
async def create_genero(request:RequestExamen, db:Session=Depends(getDB)):
    _examen = crud.create_examen(db, request.parameter)
    return Response(code=200, status='ok', message='se ha creado un examen', result=_examen).dict(exclude_none=True)

@router_examen.get('/get')
async def get_examenes(db:Session=Depends(getDB)):
    _examenes = crud.get_examenes(db, 0, 100)
    return Response(code=200, status='ok', message='se trajo todas los examenes', result=_examenes).dict(exclude_none=True)

@router_examen.get('/get/{id}')
async def get_genero_id(id:int, db:Session=Depends(getDB)):
    _examen = crud.get_examen_id(db, id)
    return Response(code=200, status='ok', message='se trajo un examen', result=_examen).dict(exclude_none=True)

# @router_genero.post('/update')
# async def update_genero(request:RequestExamen, db:Session=Depends(getDB)):
#     _examen = crud.update_genero(db, request.parameter)
#     return Response(code=200, status='ok', message='se actualizo una genero', result=_examen).dict(exclude_none=True)

# @router_genero.delete('/delete/{id}')
# async def delete_genero(id:int, db:Session=Depends(getDB)):
#     crud.delete_genero(db, id)
#     return Response(code=200, status='ok', message='se elimino un genero').dict(exclude_none=True)
