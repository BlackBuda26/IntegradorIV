import psycopg2


# Conexión a la base de datos PostgreSQL en ElephantSQL
conn = psycopg2.connect(
    dbname="tnoinmky",
    user="tnoinmky",
    password="O64c7I4rRU8JYbAjQzXkI66n9grGB_16",
    host="jelani.db.elephantsql.com",
    port="5432"  # Puerto predeterminado para PostgreSQL
)

