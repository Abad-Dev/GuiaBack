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


class KeywordQuery(BaseModel):
    keyword: str