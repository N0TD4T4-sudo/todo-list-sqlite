from flask import Flask , render_template , request , redirect
import os
import sqlite3

app = Flask(__name__)

@app.route("/" , methods=["GET", "POST"])
def inicio():
    Ruta = os.path.join(os.path.dirname(__file__),"Tareas.db")
    Base = sqlite3.connect(Ruta)
    Indexb = Base.cursor()
    Indexb.execute("""SELECT * FROM tareas""")
    Result = Indexb.fetchall()
    if request.method == "POST":
        nombre = request.form["Agregar"]
        TxT = nombre.strip()
        if TxT:
            NT = (TxT,0)
            Indexb.execute("""INSERT INTO tareas (descripcion,completada) VALUES (?,?) """ ,NT)
            Base.commit()
        return redirect("/")
    return render_template("index.html" , tareas=Result)
app.run(debug=True)