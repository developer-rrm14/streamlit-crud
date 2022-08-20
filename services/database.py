import psycopg2

DB_HOST = 'localhost'
DB_DATABASE = 'db-streamlit'
DB_USERNAME = 'postgres'
DB_PASSWORD = 'admin'
DB_PORT = 5432


conn = psycopg2.connect(
    host=DB_HOST,
    dbname=DB_DATABASE,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    port=DB_PORT)
cursor = conn.cursor()

