from fastapi import APIRouter
from db import init_connection
from models import RelationQuery, DeleteQuery

router = APIRouter()


@router.delete('/anunciante')
def delete_anunciante(query: DeleteQuery):
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'DELETE FROM REL_DISTRITOS_ANUNCIANTES WHERE FK_ANUNCIANTE = %s', query.id
        )
        cursor.execute(
            'DELETE FROM ANUNCIANTES WHERE ID = %s', query.id, 
        )
    conn.commit()
    conn.close()


@router.delete('/rel-distritos-anunciantes')
def delete_rel_distrito(query: RelationQuery):
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'DELETE FROM REL_DISTRITOS_ANUNCIANTES WHERE FK_DISTRITO = %s AND FK_ANUNCIANTE = %s;', 
            (query.fk1, query.fk2)
        )
    conn.commit()
    conn.close()


@router.delete('/rel-sub-anunciantes')
def delete_rel_distrito(query: RelationQuery):
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'DELETE FROM REL_SUB_ANUNCIANTES WHERE FK_SUB_RUBRO = %s AND FK_ANUNCIANTE = %s;', 
            (query.fk1, query.fk2)
        )
    conn.commit()
    conn.close()


@router.delete('/rel-sub-kw')
def delete_rel_sub_kw(query: RelationQuery):
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'DELETE FROM REL_SUB_KW WHERE FK_SUB_RUBRO = %s AND FK_KEYWORD = %s;', 
            (query.fk1, query.fk2)
        )
    conn.commit()
    conn.close()