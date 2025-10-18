import psycopg
import os
from dotenv import load_dotenv
from contextlib import contextmanager

load_dotenv()

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

CONN_INFO = f"dbname={db_name} user={db_user} password={db_pass} host={db_host} port={db_port}"

@contextmanager
def get_db_connection():

    conn = None

    try:
        conn = psycopg.connect(CONN_INFO)
        yield conn

    except psycopg.Error as e:
        print(f"Erro de banco de dados: {e}")

        raise
    finally:

        if conn:
            conn.close()