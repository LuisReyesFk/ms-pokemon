from fastapi import FastAPI
from .routers import pokemons

# Crear la instancia de FastAPI
app = FastAPI()

# Incluir el router de usuarios
app.include_router(pokemons.router)
