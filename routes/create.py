from fastapi import APIRouter
from db import init_connection
from models import RubroQuery, SubRubroQuery, WordQuery

router = APIRouter()

@router.post('/rubro')
def create_rubro(rubro: RubroQuery):
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'INSERT INTO RUBROS (NAME, SLUG, IMAGE) VALUES (%s, %s, %s)', 
            (rubro.name, rubro.slug, rubro.image)
        )
    conn.commit()
    conn.close()


@router.post('/sub-rubro')
def create_rubro(sub_rubro: SubRubroQuery):
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'INSERT INTO SUB_RUBROS (RUBRO_ID, NAME, SLUG, DESCRIPTION) VALUES (%s, %s, %s, %s)', 
            (sub_rubro.rubro_id, sub_rubro.name, sub_rubro.slug, sub_rubro.desc)
        )
    conn.commit()
    conn.close()


@router.post('/keyword')
def create_keyword(keyword: WordQuery):
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'INSERT INTO KEYWORDS (KEYWORD) VALUES (%s)', 
            (keyword.word).upper()
        )
    conn.commit()
    conn.close() 


@router.post('/invalid_words')
def create_invalid_word(invalid_word: WordQuery):
    conn = init_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            'INSERT INTO INVALID_WORDS (WORD) VALUES (%s)', 
            (invalid_word.word).upper()
        )
    conn.commit()
    conn.close() 