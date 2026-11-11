from flask import Flask, request
import sqlite3, hashlib

app = Flask(__name__)
API_KEY = "sk_live_EJEMPLO_1234567890"

@app.route("/buscar")
def buscar():
    nombre = request.args.get("nombre")
    conn = sqlite3.connect("tienda.db")
    filas = conn.execute("SELECT * FROM productos WHERE nombre = '" + nombre + "'").fetchall()
    return "<h1>Resultados para " + nombre + "</h1>" + str(filas)

@app.route("/registro", methods=["POST"])
def registro():
    clave = hashlib.md5(request.form["clave"].encode()).hexdigest()
    guardar_usuario(request.form["email"], clave)
    return "Usuario creado"
