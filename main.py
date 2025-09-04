# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Crear la aplicación FastAPI
app = FastAPI(
    title="Mi API Unificada",
    description="Ejemplo de API con saludos y gestión de tareas - Fusionada",
    version="1.0.0"
)


# Sección 1: Endpoints básicos


@app.get("/")
def hello_world():
    return {"message": "¡Mi primera API FastAPI unificada!"}

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


# Sección 2: API de Tareas


# Modelo de datos
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = ""
    completed: bool = False
    created_at: Optional[str] = None

# Base de datos en memoria
tasks_db: List[Task] = []
next_id = 1

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    """Crear una nueva tarea"""
    global next_id
    
    task.id = next_id
    task.created_at = datetime.now().isoformat()
    next_id += 1
    
    tasks_db.append(task)
    return task

@app.get("/tasks", response_model=List[Task])
def get_tasks(completed: Optional[bool] = None):
    """Listar todas las tareas, opcionalmente filtrar por estado"""
    if completed is None:
        return tasks_db
    return [task for task in tasks_db if task.completed == completed]

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    """Obtener una tarea específica por ID"""
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.put("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: int):
    """Marcar una tarea como completada"""
    for task in tasks_db:
        if task.id == task_id:
            task.completed = True
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

