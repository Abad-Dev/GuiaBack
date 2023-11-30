import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

DB_PW = os.getenv("DB_PASSWORD")


def init_connection():
    try:
        connection = pymysql.connect(
            host='70.32.23.64',
            port=3306,
            user='guiacali_db',
            passwd=DB_PW,
            db='guiacali_db',
            cursorclass=pymysql.cursors.DictCursor)
        print('Connected')
    except Exception as e:
        connection = None

    return connection