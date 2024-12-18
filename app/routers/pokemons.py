from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, models, database
from ..schemas import PokemonDataSchema, MyPokemonSchema
# Crear un router para las rutas de usuarios
router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/pokemons-migration/")
def read_pokemons(payload: PokemonDataSchema, db: Session = Depends(get_db)):
    return crud.read_data(db, payload)

# Ruta para obtener todos los pockemones
@router.get("/pokemons/")
def get_pokemons(db: Session = Depends(get_db)):
    return crud.get_pokemon(db)

@router.post("/pokemons/")
def get_pokemons(payload: MyPokemonSchema, db: Session = Depends(get_db)):
    return crud.new_pokemon(
        db=db,
        name=payload.name,
        weight=payload.weight,
        height=payload.height,
        image=payload.image
        )

# @router.get("/abilities/")
# def get_pokemons(db: Session = Depends(get_db)):
#     return crud.get_abilities(db)

# @router.get("/types/")
# def get_pokemons(db: Session = Depends(get_db)):
#     return crud.get_types(db)

# @router.get("/weakness/")
# def get_pokemons(db: Session = Depends(get_db)):
#     return crud.get_weakness(db)
