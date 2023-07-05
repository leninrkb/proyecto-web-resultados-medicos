from fastapi import APIRouter, HTTPException ,Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import PersonaSchema, RequestPersona, Response
import crud

router = APIRouter()

def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/create_persona')
async def createPersona(request:RequestPersona, db:Session=Depends(getDB)):
    _persona = crud.createPersona(db, request.parameter)
    return Response(code=200, status='ok', message='se ha creado una persona', result=_persona).dict(exclude_none=True)

@router.get('/get_personas')
async def getPersonas(db:Session=Depends(getDB)):
    _personas = crud.getPersonas(db, 0, 100)
    return Response(code=200, status='ok', message='se trajo todas las personas', result=_personas).dict(exclude_none=True)

@router.get('/get_persona_id/{id}')
async def getPersonaId(id:int, db:Session=Depends(getDB)):
    _persona = crud.getPersonaId(db, id)
    return Response(code=200, status='ok', message='se trajo una persona', result=_persona).dict(exclude_none=True)

@router.post('/update_persona')
async def updatePersona(request:RequestPersona, db:Session=Depends(getDB)):
    _persona = crud.updatePersona(db, request.parameter)
    return Response(code=200, status='ok', message='se actualizo una persona', result=_persona).dict(exclude_none=True)

@router.delete('/delete_persona/{id}')
async def updatePersona(id:int, db:Session=Depends(getDB)):
    crud.deletePersona(db, id)
    return Response(code=200, status='ok', message='se elimino una persona').dict(exclude_none=True)
