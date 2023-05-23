from flask import Flask, render_template, jsonify 
import mysql.connector

app = Flask(__name__)

#conexion a MySLQ
host = "localhost"
database = "bdbionika"
username = "root"
password = ""

#funcion conexion
def conexion():
    conn = mysql.connector.connect(host = host, database = database, username = username, password = password)
    return conn
    

@app.route("/home")
def home():
    return render_template("home.html")

#obtener usuarios
@app.get("/usuarios")
def get_users():
    conn = conexion()
    cursor = conn.cursor()
    sql = 'SELECT * FROM usuarios'
    cursor.execute(sql)
    datos = cursor.fetchall()  # obtener todos los datos de la consulta
    usuarios = []
    for fila in datos:
        usuario = {'nombres': fila[0], 'telefono': fila[1]}
        usuarios.append(usuario)
    cursor.close()
    conn.close()

    return jsonify({'usuarios': usuarios})   


@app.route("/usuario")
def usuario():
    return "es es la ruta de usuarios"    

@app.route("/formulario")
def formulario():
    return "llena el formulario para continuar"

@app.route("/formulario/diligenciar")
def diligenciar():
    return "diligencia el formulario"    

if __name__ =="__main__":
    app.run()    