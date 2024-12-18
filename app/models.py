from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

pokemon_type = Table(
    'pokemon_type',
    Base.metadata,
    Column('pokemon_id', Integer, ForeignKey('pokemon.id'), primary_key=True),
    Column('type_id', Integer, ForeignKey('type.id'), primary_key=True)
)

pokemon_weakness = Table(
    'pokemon_weakness',
    Base.metadata,
    Column('pokemon_id', Integer, ForeignKey('pokemon.id'), primary_key=True),
    Column('weakness_id', Integer, ForeignKey('weakness.id'), primary_key=True)
)

class Pokemon(Base):
    __tablename__ = 'pokemon'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    height = Column(Float)
    weight = Column(Float)
    experience = Column(Integer)
    image = Column(String, nullable=False)
    types = relationship("Type", secondary=pokemon_type, back_populates="pokemones")
    weakness = relationship("Weakness", secondary=pokemon_weakness, back_populates="pokemones")

class Type(Base):
    __tablename__ = 'type'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    pokemones = relationship("Pokemon", secondary=pokemon_type, back_populates="types")

class Weakness(Base):
    __tablename__ = 'weakness'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    pokemones = relationship("Pokemon", secondary=pokemon_weakness, back_populates="weakness")


class Abilities(Base):
    __tablename__ = 'abilities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
