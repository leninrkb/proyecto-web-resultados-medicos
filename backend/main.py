from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import getDB
from sqlalchemy.orm import Session
from router.personaRouter import router_persona
from router.generoRouter import router_genero
from router.rolUsuarioRouter import router_rol_usuario
from router.usuarioRouter import router_usuario
from router.examenRouter import router_examen


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/')
def home():
    return {'mensaje':'hey bro, cambiate a python :D'}

@app.get('/rollback')
def rollback(db:Session=Depends(getDB)):
    db.rollback()
    return {'rollback done'}

@app.get('/commit')
def commit(db:Session=Depends(getDB)):
    db.commit()
    return {'commit done'}

app.include_router(router_persona, prefix='/persona', tags=['persona'])
app.include_router(router_genero, prefix='/genero', tags=['genero'])
app.include_router(router_rol_usuario, prefix='/rol_usuario', tags=['rol_usuario'])
app.include_router(router_usuario, prefix='/usuario', tags=['usuario'])
app.include_router(router_examen, prefix='/examen', tags=['examen'])