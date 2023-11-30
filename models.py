from pydantic import BaseModel


class RubroQuery(BaseModel):
    name: str
    slug: str
    image: bytes


class SubRubroQuery(BaseModel):
    rubro_id: int
    name: str
    slug: str
    desc: str


class DistritoQuery(BaseModel):
    name: str


class WordQuery(BaseModel):
    word: str


class RelationQuery(BaseModel):
    fk1: int
    fk2: int


class DeleteQuery(BaseModel):
    id: int