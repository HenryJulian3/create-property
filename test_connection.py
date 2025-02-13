import psycopg2
import os

# URL de conexión
DATABASE_URL = "postgresql://postgres:BASEproperties@propertiesdb.cngsycm0ahs7.us-east-1.rds.amazonaws.com/reservabnb"

try:
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT NOW();")  # Comprobar conexión ejecutando una consulta simple
    result = cur.fetchone()
    print("✅ Conexión exitosa a PostgreSQL en AWS RDS. Hora del servidor:", result[0])
    cur.close()
    conn.close()
except Exception as e:
    print("❌ Error conectando a la base de datos:", e)
