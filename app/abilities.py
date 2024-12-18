from sqlalchemy.orm import Session
from . import models

def get_abilities(db: Session):
    return db.query(models.Abilities).all()

def new_abilities(db: Session, name: str):
    exist = db.query(models.Abilities).filter(models.Abilities.name == name).all()
    if exist:
        return { "message": f"Abilities '{name}' already exist"}
    else:
        db_save = models.Abilities(name=name)
        db.add(db_save)
        db.commit()
        db.refresh(db_save)
        return { "message": f"Abilities '{name}' successfully added"}
