from fastapi import APIRouter, HTTPException ,Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import RequestPersona, Response
from crud import personaCrud as crud

router_persona = APIRouter()

def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router_persona.post('/create')
async def createPersona(request:RequestPersona, db:Session=Depends(getDB)):
    _persona = crud.createPersona(db, request.parameter)
    return Response(code=200, status='ok', message='se ha creado una persona', result=_persona).dict(exclude_none=True)

@router_persona.get('/get')
async def getPersonas(db:Session=Depends(getDB)):
    _personas = crud.getPersonas(db, 0, 100)
    return Response(code=200, status='ok', message='se trajo todas las personas', result=_personas).dict(exclude_none=True)

@router_persona.get('/get/{id}')
async def getPersonaId(id:int, db:Session=Depends(getDB)):
    _persona = crud.getPersonaId(db, id)
    return Response(code=200, status='ok', message='se trajo una persona', result=_persona).dict(exclude_none=True)

@router_persona.post('/update')
async def updatePersona(request:RequestPersona, db:Session=Depends(getDB)):
    _persona = crud.updatePersona(db, request.parameter)
    return Response(code=200, status='ok', message='se actualizo una persona', result=_persona).dict(exclude_none=True)

@router_persona.delete('/delete/{id}')
async def updatePersona(id:int, db:Session=Depends(getDB)):
    crud.deletePersona(db, id)
    return Response(code=200, status='ok', message='se elimino una persona').dict(exclude_none=True)
