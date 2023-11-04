# Importar el modulo
from fastapi import FastAPI, Body
from db import datos
from schemas import movie as mv

# Crear la aplicación: creando una Instancia de fastapi
app = FastAPI()

# Documentación con Swagger
app.title = "First Application Programming Interface with FastApi"
app.version = "0.0.2"

data = datos.data

# Creando un primer endpoint
@app.get('/', tags = ['Home'])
def message():
    return "Learning about fastApi"

# Método GET
@app.get('/movies', tags = ['Movies'], summary= "Get all movies")
def get_movies():
    return data

# Parámetros de ruta
@app.get(path= '/movies/{id}', tags = ["Movies"], summary= "Get one movie")
def get_movie(id: int):
    try:
        return [movie for movie in data if movie['id'] == id][0]
    except IndexError:
        return {'Error' : 'Movie not found!'}
    
# Parametros query
@app.get(path= "/movies/", summary="Get movie by category", tags = ["Movies"])
def get_movie_by_category(category: str):
    try:
        return [ movies for movies in data if movies['genre'] == category ]
    except IndexError:
        return {"Error": "Movies in that category not found!"}
    
# Método POST
@app.post(path = "/movies", tags = ["Movies"], summary= "Add a new movie to films")
def register_movie(new_movie: mv.Movie):
    data.append(dict(new_movie))
    return new_movie

# Método PUT
@app.put(path = "/movies/{id}", tags = ["Movies"], summary = "Update movie")
def update_movie(id: int, film: mv.Movie):
    for movie in data:
        if movie['id'] == id:
            movie['title'] = film.title
            movie['year'] =  film.year
            movie['genre'] = film.genre
            movie['director'] = film.director
            movie['rating'] =  film.rating
            return data
        
# Método DELETE
@app.delete(path = "/movies/{id}", tags = ["Movies"], summary= "Delete a movie")
def delete_movie(id: int):
    for movie in data:
        if movie['id'] == id:
            data.remove(movie)