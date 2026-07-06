from flask import Flask, jsonify, request
from db import Database

app = Flask(__name__)

# ==========================
# LISTAR PRODUCTOS
# ==========================
@app.route("/productos", methods=["GET"])
def listar_productos():
    db = Database()
    data = db.execute(
        "SELECT id, nombre, precio, activo, fecha_de_creacion FROM productos"
    )
    db.close()
    return jsonify(data)

# ==========================
# OBTENER PRODUCTO POR ID
# ==========================
@app.route("/productos/<int:id>", methods=["GET"])
def obtener_producto(id):
    db = Database()
    data = db.execute(
        "SELECT id, nombre, precio, activo, fecha_de_creacion FROM productos WHERE id=%s",
        (id,)
    )
    db.close()
    return jsonify(data)

# ==========================
# CREAR PRODUCTO
# ==========================
@app.route("/productos", methods=["POST"])
def crear_producto():
    data = request.json
    db = Database()

    db.execute(
        """
        INSERT INTO productos(nombre, precio, activo)
        VALUES (%s, %s, %s)
        """,
        (
            data["nombre"],
            data["precio"],
            data["activo"]
        )
    )
    db.close()

    return jsonify({
        "mensaje": "Producto creado con éxito"
    }), 201

# ==========================
# ACTUALIZAR PRODUCTO
# ==========================
@app.route("/productos/<int:id>", methods=["PUT"])
def actualizar_producto(id):
    data = request.json
    db = Database()

    db.execute(
        """
        UPDATE productos
        SET nombre=%s,
            precio=%s,
            activo=%s
        WHERE id=%s
        """,
        (
            data["nombre"],
            data["precio"],
            data["activo"],
            id
        )
    )
    db.close()

    return jsonify({
        "mensaje": "Producto actualizado con éxito"
    })

# ==========================
# ELIMINAR PRODUCTO
# ==========================
@app.route("/productos/<int:id>", methods=["DELETE"])
def eliminar_producto(id):
    db = Database()
    db.execute(
        "DELETE FROM productos WHERE id=%s",
        (id,)
    )
    db.close()

    return jsonify({
        "mensaje": "Producto eliminado con éxito"
    })

# ==========================
# INICIAR APLICACIÓN
# ==========================
if __name__ == "__main__":
    app.run(debug=True)
