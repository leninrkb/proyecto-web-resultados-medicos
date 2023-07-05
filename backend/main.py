from fastapi import FastAPI
from config import engine
import models
import router

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()
@app.get('/')
def home():
    return {'mensaje':'hey bro, cambiate a python :D'}

app.include_router(router.router, prefix='/exam', tags=['exam'])