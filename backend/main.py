from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Modelos
class User(BaseModel):
    username: str
    password: str
    is_admin: bool = False
    invested: float = 0.0
    earnings: float = 0.0
    history: List[str] = []

# Usuarios de prueba
users_db = {
    "admin": User(username="admin", password="admin123", is_admin=True),
    "user1": User(username="user1", password="user123", invested=1000, earnings=150, history=["Depósito $1000"]),
}

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or user.password != form_data.password:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/me")
def get_me(token: str = Depends(oauth2_scheme)):
    user = users_db.get(token)
    if not user:
        raise HTTPException(status_code=401, detail="Token inválido")
    return user

@app.get("/admin/users")
def get_users(token: str = Depends(oauth2_scheme)):
    user = users_db.get(token)
    if not user or not user.is_admin:
        raise HTTPException(status_code=403, detail="No autorizado")
    return list(users_db.values())

@app.get("/")
def root():
    return {"message": "API Club de Inversores MVP"}
