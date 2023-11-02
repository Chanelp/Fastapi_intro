# Importar el modulo
from fastapi import FastAPI

# Crear la aplicación: creando una Instancia de fastapi
app = FastAPI()

# Documentación con Swagger
app.title = "First Application Programming Interface with FastApi"
app.version = "0.0.2"

movies = [
     {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

# Creando un primer endpoint
@app.get('/', tags = ['Home'])
def message():
    return "Learning about fastApi"

@app.get('/movies', tags = ['Movies'])
def get_movies():
    return movies