from fastapi import APIRouter
from db import init_connection

router = APIRouter()


@router.get('/anunciante-noimg')
def get_partial_anunciantes():
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT ID, NAME FROM ANUNCIANTES ORDER BY ID DESC'
        )
    anunciantes = cursor.fetchall()
    conn.close()
    return anunciantes


@router.get('/anunciante')
def get_partial_anunciantes():
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM ANUNCIANTES ORDER BY NAME ASC'
        )
    anunciantes = cursor.fetchall()
    conn.close()
    return anunciantes


@router.get('/rubro-noimg')
def get_partial_rubros():
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT ID, NAME, SLUG FROM RUBROS ORDER BY ID DESC'
        )
    rubros = cursor.fetchall()
    conn.close()
    return rubros


@router.get('/rubro')
def get_complete_rubros():
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM RUBROS'
        )
    rubros = cursor.fetchall()
    conn.close()
    return rubros


@router.get('/sub-rubro')
def get_sub_rubros():
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM SUB_RUBROS'
        )
    sub_rubros = cursor.fetchall()
    conn.close()
    return sub_rubros


@router.get('/rel-sub-anunciantes')
def get_rel_sub_anunciantes():
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM REL_SUB_ANUNCIANTES'
        )
    rels = cursor.fetchall()
    conn.close()
    return rels



@router.get('/distrito')
def get_distritos():
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM DISTRITOS'
        )
    distritos = cursor.fetchall()
    conn.close()
    return distritos



@router.get('/keyword')
def get_keyword():
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM KEYWORDS'
        )
    keywords = cursor.fetchall()
    conn.close()
    return keywords



@router.get('/invalid-words')
def get_invalid_words():
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM INVALID_WORDS'
        )
    words = cursor.fetchall()
    conn.close()
    return words



@router.get('/rel-distritos-anunciantes')
def get_relate_distritos():
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM REL_DISTRITOS_ANUNCIANTES'
        )
    rels = cursor.fetchall()
    conn.close()
    return rels


@router.get('/rel-sub-kw')
def get_relate_distritos():
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM REL_SUB_KW'
        )
    rels = cursor.fetchall()
    conn.close()
    return rels


# Single Functions
@router.get('/anunciante/{id}')
def get_anunciante_rubro_by_id(id):
    if not id:
        return
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM ANUNCIANTES WHERE ID = %s',
        id)   
    anunciante = cursor.fetchone()
    conn.close()
    return anunciante

@router.get('/rubro-noimg/{id}')
def get_partial_rubro_by_id(id):
    if not id:
        return
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT ID, NAME, SLUG FROM RUBROS WHERE ID = %s',
        id)   
    rubro = cursor.fetchone()
    conn.close()
    return rubro



