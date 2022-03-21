from http import client
import MySQLdb
import psycopg2
from pymongo import MongoClient


# mysql
conn = MySQLdb.connect(
    user='root',
    passwd='password',
    host='localhost',
    db='mysql'
)
# SQL実行
conn.close


# PostgreSQL
user = 'root'
password = 'password'
host = 'localhost'
port = 5432
db = 'postgres'
conn = psycopg2.connect(
    f'postgresql://{user}:{password}@{host}:{port}/{db}'
)
# SQL実行
conn.close()


#MongoDB
client = MongoClient('mongodb://localhost:5432/')
db = client['db_name']

data = {
    'a': 1,
    'b': 2
}

db_stack = db.stacks
stack_id = db_stack.insert_one(data).inserted_id
