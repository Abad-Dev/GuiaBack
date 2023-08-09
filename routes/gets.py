from fastapi import APIRouter
from db import init_connection

router = APIRouter()


@router.get('/rubro-noimg')
def get_partial_rubro():
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT ID, NAME, SLUG FROM RUBROS'
        )
    rubros = cursor.fetchall()
    conn.close()
    return rubros


@router.get('/rubro')
def get_complete_rubro():
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM RUBROS'
        )
    rubros = cursor.fetchall()
    conn.close()
    return rubros


@router.get('/sub-rubro')
def get_sub_rubro():
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM SUB_RUBROS'
        )
    sub_rubros = cursor.fetchall()
    conn.close()
    return sub_rubros


@router.get('/distrito')
def get_distrito():
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
            'SELECT * FROM DISTRITOS'
        )
    distritos = cursor.fetchall()
    conn.close()
    return distritos






