# Importar el modulo
from fastapi import FastAPI

import db

# Crear la aplicación: creando una Instancia de fastapi
app = FastAPI()

# Documentación con Swagger
app.title = "First Application Programming Interface with FastApi"
app.version = "0.0.2"

data = [
        {
            "id": 1,
            "title": "The Galactic Adventure",
            "year": 2020,
            "genre": "Sci-Fi",
            "director": "John Director",
            "rating": 8.0
        },
        {
            "id": 2,
            "title": "La Gran Comedia",
            "year": 2019,
            "genre": "Comedy",
            "director": "Maria Director",
            "rating": 7.5
        },
        {
            "id": 3,
            "title": "Drama in the City",
            "year": 2021,
            "genre": "Drama",
            "director": "Michael Director",
            "rating": 8.5
        },
        {
            "id": 4,
            "title": "Mystery Island",
            "year": 2018,
            "genre": "Mystery",
            "director": "Emma Director",
            "rating": 9.0
        },
        {
            "id": 5,
            "title": "Aventura Extrema",
            "year": 2022,
            "genre": "Adventure",
            "director": "Daniel Director",
            "rating": 7.8
        }
    ]

# Creando un primer endpoint
@app.get('/', tags = ['Home'])
def message():
    return "Learning about fastApi"

# Método GET
@app.get('/movies', tags = ['Movies'])
def get_movies():
    return data

# Parámetros de ruta
@app.get('/movies/{id}', tags = ["Movies"])
def get_movie(id: int):
    try:
        return [movie for movie in data if movie['id'] == id][0]
    except IndexError:
        return {'Error' : 'Movie not found!'}