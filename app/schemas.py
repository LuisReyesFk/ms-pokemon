from pydantic import BaseModel, HttpUrl
from typing import List, Dict

class PokemonSchema(BaseModel):
    abilities: List[str]
    detailPageURL: str
    weight: float
    weakness: List[str]
    number: str
    height: float
    collectibles_slug: str
    featured: str
    slug: str
    name: str
    ThumbnailAltText: str
    image: str
    id: int
    type: List[str]

class PokemonDataSchema(BaseModel):
    data: List[PokemonSchema]

class MyPokemonSchema(BaseModel):
    name: str
    weight: float
    height: float
    image: str
