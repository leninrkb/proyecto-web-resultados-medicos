from fastapi import FastAPI
from router.personaRouter import router_persona
from router.generoRouter import router_genero

app = FastAPI()
@app.get('/')
def home():
    return {'mensaje':'hey bro, cambiate a python :D'}

app.include_router(router_persona, prefix='/persona', tags=['persona'])
app.include_router(router_genero, prefix='/genero', tags=['genero'])