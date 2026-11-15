# To-do list

## Proyecto de aprendizaje

Es una to-do list con dos versiones: una web (Flask) y una de consola.

En el navegador se pueden **ver** las tareas y **agregar** nuevas. En esta versión aún no se pueden completar tareas desde la web.

La versión de consola tiene 5 funciones:
- Agregar tarea
- Ver tareas
- Cambiar estado (completar tareas)
- Borrar tarea
- Editar tarea (cambiar la descripción)

Para ejecutarlo se necesita tener Python 3. El script crea una base de datos (SQLite) donde se guardan todas las tareas, y si ya está creada, usa esa.

## Cómo instalar

```
pip install -r requirements.txt
```

## Cómo usar

Para iniciar la versión web se usa el comando:

```
python app.py
```

Con esto se entra por defecto a http://127.0.0.1:5000. Si no funciona el enlace, en la terminal aparecerá el enlace correspondiente. Todo se ejecuta de manera local.

## Versión en consola

```
python todo.py
```