# ms-pokemon
## Run migrate

alembic revision --autogenerate -m "Creación inicial de tablas de Pokémon"
alembic upgrade head

## Run project
Posicionandose en la raíz del proyecto:
1. cd /app
2. fastapi dev main.py

## Docs url
http://127.0.0.1:8000/docs