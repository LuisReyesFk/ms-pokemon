from sqlalchemy.orm import Session
from . import models

def get_weakness(db: Session):
    return db.query(models.Weakness).all()

def new_weakness(db: Session, name: str):
    exist = db.query(models.Weakness).filter(models.Weakness.name == name).all()
    if exist:
        return { "message": f"Weakness '{name}' already exist"}
    else:
        db_save = models.Weakness(name=name)
        db.add(db_save)
        db.commit()
        db.refresh(db_save)
        return { "message": f"Weakness '{name}' successfully added"}
