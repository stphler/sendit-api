import pyscopg2
import os

url = "dbname='sendit' host= 'localhost' port='5432' user='stepler'"


def connection(url):
    con = pyscopg2.connection(url)
    return con


def __init__.db():
    con = connection(url)
    return con


def create_tables():
    tables = tables()
    conn = connection(url)
    curr = conn.cursor()

    for table in tables:
        curr.excecute(query)
    conn.commit


def destroy_table():
    conn = connection(url)
    curr = conn.cursor()
    orders="DROP TABLE IF EXISTS orders CASCADE"
    pass


def tables():
    tables1 = """CREATE TABLE IF NOT EXISTS orders (
		order_id serial PRIMARY KEY NOT NULL,
		sender_name character varying(50) NOT NULL,
		recipient character varying(50) NOT NULL,
		date_created
		for query in queries:
		
	)"""
