# Importar el modulo
from fastapi import FastAPI, Body, Path, Query, status, Depends
from fastapi.responses import JSONResponse
from typing import Any, Coroutine, List, Optional

from db import datos
from schemas import movie as mv
from schemas import user as us
from jwt_manager import create_token, JWTBearer

# Crear la aplicación: creando una Instancia de fastapi
app = FastAPI()

# Documentación automática con Swagger
app.title = "First Application Programming Interface with FastApi"
app.version = "0.0.2"

movies = datos.movies

# Creando un primer endpoint
@app.get('/', tags = ['Home'])
def message():
    return "Learning about fastApi"

# Método GET
@app.get('/movies', tags = ['Movies'], summary= "Get all movies", response_model = List[mv.Movie], dependencies= [Depends(JWTBearer())])
def get_movies() -> List[mv.Movie]:
    return JSONResponse(content = movies)

# Parámetros de ruta
@app.get(path= '/movies/{id}', tags = ["Movies"], summary= "Get one movie", response_model = mv.Movie)
def get_movie(id: int =  Path(ge=1, le=200)) -> mv.Movie:
    try:
        movie_found = [movie for movie in movies if movie['id'] == id][0]
        return JSONResponse(content= movie_found)
    except IndexError:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content= [])
    
# Parametros query
@app.get(path= "/movies/", summary="Get movie by category", tags = ["Movies"], response_model = List[mv.Movie], status_code= status.HTTP_200_OK)
def get_movie_by_category(category: str = Query(min_length= 5, max_length= 15)) -> List[mv.Movie]:
    try:
        data = [ movies for movies in movies if movies['genre'] == category ]
        return JSONResponse(content= data, status_code= status.HTTP_200_OK)
    except IndexError:
        return {"Error": "Movies in that category not found!"}
    
# Método POST
@app.post(path = "/movies", tags = ["Movies"], summary= "Add a new movie to films", response_model= dict, status_code=status.HTTP_201_CREATED)
def register_movie(new_movie: mv.Movie) -> dict:
    movies.append(dict(new_movie))
    return JSONResponse(content = {"message":"Movie sucessfully registered!"}, status_code= status.HTTP_201_CREATED)

# Login
@app.post(path= "/login", tags = ["Auth"], summary= "Log In")
def login(user: us.user):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token = create_token(user.model_dump())
        return JSONResponse(status_code= status.HTTP_200_OK, content= token)
    else:
        return JSONResponse(status_code= status.HTTP_401_UNAUTHORIZED, content= {"message":"Credenciales inválidas, intente de nuevo"})

# Método PUT
@app.put(path = "/movies/{id}", tags = ["Movies"], summary = "Update movie", response_model = dict, status_code= status.HTTP_200_OK)
def update_movie(id: int, film: mv.Movie) -> dict:
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = film.title
            movie['year'] =  film.year
            movie['genre'] = film.genre
            movie['director'] = film.director
            movie['rating'] =  film.rating
            return JSONResponse(content = {"message":"Movie successfully updated!"})
        
# Método DELETE
@app.delete(path = "/movies/{id}", tags = ["Movies"], summary= "Delete a movie", response_model = dict, status_code= status.HTTP_200_OK)
def delete_movie(id: int) -> dict:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return JSONResponse(content= {"message":"Movie successfully removed!"}, status_code= status.HTTP_200_OK)