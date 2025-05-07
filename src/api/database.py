# from dotenv import load_dotenv

from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.abstracts import MySQLConnectionAbstract
import mysql.connector
import os

# load_dotenv()  # Carga el archivo .env automáticamente


# def get_connection():
#     return mysql.connector.connect(
#         host=os.getenv("DB_HOST"),
#         port=int(os.getenv("DB_PORT")),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         database=os.getenv("DB_NAME")
#     )

def get_connection() -> PooledMySQLConnection | MySQLConnectionAbstract:
    return mysql.connector.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ["DB_PORT"]),
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"]
    )
