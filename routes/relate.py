from fastapi import APIRouter
from db import init_connection
from models import RelationQuery

router = APIRouter()

@router.put('/rel-sub-anunciantes')
def relation_sub_anunciantes(query: RelationQuery):
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'INSERT INTO REL_SUB_ANUNCIANTES (FK_SUB_RUBRO, FK_ANUNCIANTE) VALUES (%s, %s)', 
            (query.fk1, query.fk2)
        )
    conn.commit()
    conn.close()


@router.put('/rel-sub-kw')
def relation_sub_keywords(query: RelationQuery):
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'INSERT INTO REL_SUB_KW (FK_SUB_RUBRO, FK_KEYWORD) VALUES (%s, %s)', 
            (query.fk1, query.fk2)
        )
    conn.commit()
    conn.close()


@router.put('/rel-sub-anunciantes')
def relation_sub_anunciantes(query: RelationQuery):
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'INSERT INTO REL_SUB_ANUNCIANTES (FK_SUB_RUBRO, FK_ANUNCIANTE) VALUES (%s, %s)', 
            (query.fk1, query.fk2)
        )
    conn.commit()
    conn.close()


@router.put('/rel-distritos-anunciantes')
def relation_sub_keywords(query: RelationQuery):
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'INSERT INTO REL_DISTRITOS_ANUNCIANTES (FK_DISTRITO, FK_ANUNCIANTE) VALUES (%s, %s)', 
            (query.fk1, query.fk2)
        )
    conn.commit()
    conn.close()