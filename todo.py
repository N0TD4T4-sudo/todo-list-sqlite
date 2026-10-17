import sqlite3
import os
Ruta = os.path.join(os.path.dirname(__file__),"tareas.db")
print(Ruta)
Base = sqlite3.connect("Tareas.db")
Indexb = Base.cursor()
Indexb.execute("""CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT,
    completada INTEGER )""")
def agregar_tarea ():
    Nt = input("Introducir Nombre de la tarea\n")
    New_Task = (Nt,0)
    Indexb.execute("""INSERT INTO tareas (descripcion,completada) VALUES (?,?) """ ,New_Task)
    Base.commit()
def Ver_tareas ():   
    Indexb.execute(""" SELECT * FROM tareas""")
    resultado = Indexb.fetchall()
    for ID ,tarea,Estado in resultado:
        print(ID,tarea,Estado)
def Cambiar_estado():
    Nw = int(input("Que tarea completaste ? \n"))
    Indexb.execute("""UPDATE tareas SET completada =  1 WHERE ID = ? """, (Nw,))
    Base.commit()
def Borrar_tarea():
    ND = int(input("Que tarea desea eliminar ? \n"))
    Indexb.execute("""DELETE FROM tareas WHERE ID = ? """, (ND,))
    Base.commit()
def Editar_tarea():
    NT = int(input("Introduzca el indice de la tarea"))
    ND = input("Introduzca el nuevo nombre\n")
    Indexb.execute("""UPDATE tareas set descripcion = ?  WHERE ID = ? """, (ND,NT))
    Base.commit()
while True:
    print ("""Elegir una opcion 
    1. Agregar Tarea 
    2. Ver Tareas
    3. Completar
    4. Editar tarea
    5. Borrar tarea
    6. Salir """)
    try:
        option = int(input("\n"))
    except ValueError:
        print("eso no es un numero")
        continue
    if option > 6 or option < 1:
        print("El numero no se encuentra dentro de las opciones")
        continue
    else:
        if option == 1 :
            agregar_tarea()
        elif option == 2:
            Ver_tareas()
        elif option == 3:
            Cambiar_estado()
        elif option == 5:
            Borrar_tarea()
        elif option ==4:
            Editar_tarea()
        elif option == 6:
            break
            



