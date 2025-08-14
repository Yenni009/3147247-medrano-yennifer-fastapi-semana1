from fastapi import FastAPI

# Crear la aplicación (lo más simple posible)
app = FastAPI(title="Mi Primera API")

# Endpoint 1: Hello World (OBLIGATORIO)
@app.get("/")
def hello_world():
    return {"message": "¡Mi primera API FastAPI!"}

# Endpoint 2: Info básica (OBLIGATORIO)
@app.get("/info")
def info():
    return {"api": "FastAPI", "week": 1, "status": "running"}

from fastapi import FastAPI

app = FastAPI(title="Mi Primera API")

@app.get("/")
def hello_world():
    return {"message": "¡Mi primera API FastAPI!"}

@app.get("/info")
def info():
    return {"api": "FastAPI", "week": 1, "status": "running"}


@app.get("/greeting/{name}/{edad}")
def greet_user(name: str, edad: int):
    return {"greeting": f"¡Hola {name} con {edad} años!"}


@app.get("/my-profile")
def my_profile():
    return {
        "name": "Yennifer",           
        "bootcamp": "FastAPI",
        "week": 1,
        "date": "2025",
        "likes_fastapi": True              
    }
