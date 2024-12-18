from sqlalchemy.orm import Session
from . import models
from .schemas import PokemonDataSchema

def get_types(db: Session):
    return db.query(models.Type).all()

def new_type(db: Session, name: str):
    exist_type = db.query(models.Type).filter(models.Type.name == name).all()
    if exist_type:
        return { "message": f"Type '{name}' already exist"}
    else:
        db_type = models.Type(name=name)
        db.add(db_type)
        db.commit()
        db.refresh(db_type)
        return { "message": f"Type '{name}' successfully added"}