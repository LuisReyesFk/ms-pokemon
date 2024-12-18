from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from . import models
from .schemas import PokemonDataSchema, MyPokemonSchema
from .types import new_type
from .weakness import new_weakness
from .abilities import new_abilities

def read_data(db: Session, payload: PokemonDataSchema):
    for pokemon in payload.data:
        # Abilities table
        for name in pokemon.weakness:
            new_abilities(db=db, name=name)
        # Weakness table
        for name in pokemon.weakness:
            new_weakness(db=db, name=name)
        # Type table
        for type in pokemon.type:
            new_type(db=db, name=type)
        # Pokemon table
        new_pokemon(db=db, data=pokemon)
        for type in pokemon.type:
            add_type_to_pokemon(db=db, pokemon_name=pokemon.name, type_name=type)
        for name in pokemon.weakness:
            add_weakness_to_pokemon(db=db, pokemon_name=pokemon.name, weakness_name=name)

    return {"message": "Pokémon procesados exitosamente"}

def get_pokemon(db: Session):
# Realiza la consulta y carga los tipos asociados a cada Pokémon
    pokemons = db.query(models.Pokemon).options(
        selectinload(models.Pokemon.types),
        selectinload(models.Pokemon.weakness)
        ).all()

    result = []
    for pokemon in pokemons:
        result.append({
            "id": pokemon.id,
            "name": pokemon.name,
            "height": pokemon.height,
            "weight": pokemon.weight,
            "image": pokemon.image,
            "type": [type.name for type in pokemon.types],
            "weakness": [weakness.name for weakness in pokemon.weakness]
        })
    return result

def new_pokemon(db: Session, data: MyPokemonSchema):
    exist = db.query(models.Pokemon).filter(models.Pokemon.name == data.name).all()
    if exist:
        return { "message": f"Pokemon '{data.name}' already exist"}
    else:
        db_user = models.Pokemon(
            name=data.name,
            weight=data.weight,
            height=data.height,
            experience=0,
            image=data.image
            )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return { "message": f"Pokemon '{data.name}' successfully added"}

def add_type_to_pokemon(db: Session, pokemon_name: str, type_name: str):
    # Verifica que el Pokémon y el Tipo existen
    pokemon = db.query(models.Pokemon).filter(models.Pokemon.name == pokemon_name).first()
    pokemon_type = db.query(models.Type).filter(models.Type.name == type_name).first()

    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokémon no encontrado")
    if not pokemon_type:
        raise HTTPException(status_code=404, detail="Tipo no encontrado")
    if pokemon_type in pokemon.types:
        return {"message": "El tipo ya está asociado a este Pokémon"}
    pokemon.types.append(pokemon_type)
    db.add(pokemon) # Asegúrate de que SQLAlchemy está siguiendo el cambio en la sesión
    db.commit() # Confirmar los cambios en la base de datos
    db.refresh(pokemon) # Refrescar para asegurarse de que los cambios están en el objeto
    return {"message": f"Type add to Pokémon id #{pokemon.id}"}

def add_weakness_to_pokemon(db: Session, pokemon_name: str, weakness_name: str):
    # Verifica que el Pokémon y el Tipo existen
    pokemon = db.query(models.Pokemon).filter(models.Pokemon.name == pokemon_name).first()
    pokemon_weakness = db.query(models.Weakness).filter(models.Weakness.name == weakness_name).first()

    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokémon no encontrado")
    if not pokemon_weakness:
        raise HTTPException(status_code=404, detail="Debilidad no encontrada")
    if pokemon_weakness in pokemon.weakness:
        return {"message": "La debilidad ya está asociado a este Pokémon"}
    pokemon.weakness.append(pokemon_weakness)
    db.add(pokemon) # Asegúrate de que SQLAlchemy está siguiendo el cambio en la sesión
    db.commit() # Confirmar los cambios en la base de datos
    db.refresh(pokemon) # Refrescar para asegurarse de que los cambios están en el objeto
    return {"message": f"Weakness add to Pokémon id #{pokemon.id}"}