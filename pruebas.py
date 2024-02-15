import psycopg2

def Conexion_BD():
    # Intenta conectarte a la base de datos
    try:
        conn = psycopg2.connect(
            host="rosie.db.elephantsql.com",
            database="vovdberw",
            user="vovdberw",
            password="6lu7q2yx-SeiyA6Nap0ikjQQXm-LEaA1"
        )
        print("Conexión exitosa a la base de datos POSTGRESSQL.")
        return conn  # Devuelve la conexión
    
    except psycopg2.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None

# Ejemplo de uso de la función Conexion_BD
conn = Conexion_BD()
if conn is not None:
    cur = conn.cursor()
    cur.execute("INSERT INTO usuarios (nombre, celular, cedula) VALUES ('Manuela Rivera', '1111111', '1231111');")
    conn.commit()
    # Ahora puedes ejecutar tus consultas utilizando el cursor
    cur.close()
    conn.close()



