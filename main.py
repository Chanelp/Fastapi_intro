# Importar el modulo
from fastapi import FastAPI

import db

# Crear la aplicación: creando una Instancia de fastapi
app = FastAPI()

# Documentación con Swagger
app.title = "First Application Programming Interface with FastApi"
app.version = "0.0.2"

# Creando un primer endpoint
@app.get('/', tags = ['Home'])
def message():
    return "Learning about fastApi"

@app.get('/movies', tags = ['Movies'])
def get_movies():
    return db.data