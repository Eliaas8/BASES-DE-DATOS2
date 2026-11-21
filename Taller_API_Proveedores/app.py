from datos_locales import CLAVE
from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)


@app.route("/proveedores", methods=["GET"])
def consultar_proveedores():

    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password=CLAVE,
        database="proveedores_db",
        port=3308
    )

    cursor = conexion.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM proveedores")
    proveedores = cursor.fetchall()
    conexion.close()

    return jsonify(proveedores)


@app.route("/proveedores", methods=["POST"])
def agregar_proveedor():

    datos = request.get_json()

    nombre = datos["nombre"]
    telefono = datos["telefono"]
    correo = datos["correo"]
    direccion = datos["direccion"]

    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password=CLAVE,
        database="proveedores_db",
        port=3308
    )

    cursor = conexion.cursor()

    sql = "INSERT INTO proveedores (nombre, telefono, correo, direccion) VALUES (%s, %s, %s, %s)"

    cursor.execute(sql, (nombre, telefono, correo, direccion))
    conexion.commit()
    conexion.close()

    return jsonify({"mensaje": "Proveedor agregado correctamente"})


@app.route("/proveedores/<int:id>", methods=["PUT"])
def modificar_proveedor(id):

    datos = request.get_json()

    nombre = datos["nombre"]
    telefono = datos["telefono"]
    correo = datos["correo"]
    direccion = datos["direccion"]

    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password=CLAVE,
        database="proveedores_db",
        port=3308
    )

    cursor = conexion.cursor()

    sql = "UPDATE proveedores SET nombre=%s, telefono=%s, correo=%s, direccion=%s WHERE id=%s"

    cursor.execute(sql, (nombre, telefono, correo, direccion, id))
    conexion.commit()
    conexion.close()

    return jsonify({"mensaje": "Proveedor modificado correctamente"})


@app.route("/proveedores/<int:id>", methods=["DELETE"])
def eliminar_proveedor(id):

    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password=CLAVE,
        database="proveedores_db",
        port=3308
    )

    cursor = conexion.cursor()

    sql = "DELETE FROM proveedores WHERE id=%s"

    cursor.execute(sql, (id,))

    conexion.commit()

    conexion.close()

    return jsonify({"mensaje": "Proveedor eliminado correctamente"})


app.run()
