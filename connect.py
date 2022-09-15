import psycopg2
from decouple import config

con = psycopg2.connect(
    database=config('database'),
    user=config('user'),
    password=config('password'),
    host=config('host'),
    port=config('port')
)

cur = con.cursor()
