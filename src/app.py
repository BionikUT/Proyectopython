from flask import Flask, render_template

app = Flask(__name__)

#conexion a MySLQ
host = "localhost"
database = "bdbionika"
username = "root"
password = ""

#funcion conexion
def conexion():
    conn = connect(host = host, database = database, username = username, password = password)
    return conn
    

@app.route("/home")
def home():
    return render_template("home.html")

#obtener usuarios
@app.get("/usuarios")
def get_users():
    conn = conexion()


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