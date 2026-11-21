from datos_locales import CLAVE
import pymysql

conexion = pymysql.connect(
    host="localhost",
    user="root",
    password=CLAVE,
    database="proveedores_db",
    port=3308
)

print("Conexion exitosa")

cursor = conexion.cursor()
cursor.execute("SELECT * FROM proveedores")
proveedores = cursor.fetchall()

for proveedor in proveedores:
    print(proveedor)

conexion.close()
