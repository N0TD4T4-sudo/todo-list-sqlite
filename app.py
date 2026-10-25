from flask import Flask
import os
import sqlite3

app = Flask(__name__)

@app.route("/")
def inicio():
    Ruta = os.path.join(os.path.dirname(__file__),"Tareas.db")
    Base = sqlite3.connect(Ruta)
    Indexb = Base.cursor()
    Indexb.execute("""SELECT * FROM tareas""")
    Result = Indexb.fetchall()
    Txt = "Tareas  -  Estado<br>"
    for ID,Task,Status in Result:
        if Status:
            Txt = Txt + f"{Task} - Completada<br>"
        else:
            Txt = Txt + f"{Task} - Por Completar<br>" 
    return Txt

app.run(debug=True)