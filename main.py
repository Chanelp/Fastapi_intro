# Importar el modulo
from fastapi import FastAPI

# Crear la aplicación: creando una Instancia de fastapi
app = FastAPI()

app.title = "First Application Programming Interface with FastApi"
app.version = "0.0.2"

# Creando un primer endpoint
@app.get('/', tags = ['Home!'])
def message():
    return "Learning about fastApi"