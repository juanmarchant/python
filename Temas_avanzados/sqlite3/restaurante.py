"""
1.1) A lo largo de estos ejercicios vamos a crear un pequeño sistema para gestionar los platos del menú de un restaurante. Por ahora debes empezar creando un script llamado restaurante.py y 
    dentro una función crear_bd() que creará una pequeña base de datos restaurante.db con las siguientes dos tablas:**

** *Si ya existen deberá tratar la excepción y mostrar que las tablas ya existen. En caso contrario mostrará que se han creado correctamente.* **
     
```sql
CREATE TABLE categoria(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(100) UNIQUE NOT NULL)
```
 
```sql
CREATE TABLE plato(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(100) UNIQUE NOT NULL, 
				categoria_id INTEGER NOT NULL,
				FOREIGN KEY(categoria_id) REFERENCES categoria(id))
```

**Nota:** *La línea **FOREIGN KEY(categoria_id) REFERENCES categoria(id)** indica un tipo de clave especial (foránea), 
        por la cual se crea una relación entre la categoría de un plato con el registro de categorías.*

** Llama a la función y comprueba que la base de datos se crea correctamente.**

**1.2) Crea una función llamada agregar_categoria() que pida al usuario un nombre de categoría y se encargue de crear la categoría en la base de datos 
    (ten en cuenta que si ya existe dará un error, por que el nombre es UNIQUE).**

** Ahora, crea un pequeño menú de opciones dentro del script, que te de la bienvenida al sistema y te permita Crear una categoría o Salir. 
    Añade las siguientes tres categorías utilizando este menú de opciones:**

- Primeros 
- Segundos 
- Postres
 
**1.3) Crea una función llamada agregar_plato() que muestre al usuario las categorías disponibles y le permita escoger una (escribiendo un número).**

**Luego le pedirá introducir el nombre del plato y lo añadirá a la base de datos, teniendo en cuenta que la categoria del plato concuerde con el id de la categoría 
    y que el nombre del plato no puede repetirse (no es necesario comprobar si la categoría realmente existe, en ese caso simplemente no se insertará el plato).**

**Agrega la nueva opción al menú de opciones y añade los siguientes platos:**

- **Primeros**: Ensalada del tiempo / Zumo de tomate
- **Segundos**: Estofado de pescado / Pollo con patatas
- **Postres**: Flan con nata / Fruta del tiempo

**1.4) Crea una función llamada mostrar_menu() que muestre el menú con todos los platos de forma ordenada: los primeros, los segundos y los postres. 
    Optativamente puedes adornar la forma en que muestras el menú por pantalla.** """


import sqlite3


def crear_db():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    # BASE DE DATOS CATEGORIA
    try:
        cursor.execute(
            "CREATE TABLE categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL)")
    except sqlite3.OperationalError:
        print("La base de datos (Categoria) ya se encuentra creada")
    else:
        print("Las base de datos (Categoria) se ha creado perfectamente")

    # BASE DE DATOS PLATO
    try:
        cursor.execute(
            "CREATE TABLE plato(id INTEGER PRIMARY KEY AUTOINCREMENT,nombre VARCHAR(100) UNIQUE NOT NULL,categoria_id INTEGER NOT NULL,FOREIGN KEY(categoria_id) REFERENCES categoria(id))")    
    except sqlite3.OperationalError:
        print("La base de datos (Plato) ya se encuentra creada")
    else:
        print("La base de datos (Plato) se creado perfectamente")

    conexion.close()

def agregar_categoria():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    opcion_categoria = input("""
    ¿Que categoria desea crear?:

    => """)
    try:
        cursor.execute(f"INSERT INTO categoria VALUES(null, '{opcion_categoria}')")
    except sqlite3.IntegrityError:
        print(f"""
    La categoria {opcion_categoria} ya se encuentra creada""")
    else:
        print(f"""
    Categoria {opcion_categoria} creada satisfactoriamente""")


    conexion.commit()
    conexion.close()


def agregar_plato():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()

    print(f"""
    Escoge una de las categorias
    """)

    for categoria in categorias:
        print(f"    {[categoria[0]]} {categoria[1]}")

    while True:
        try:
            opcion_categoria = int(input("""
        => """))
        except ValueError:
            print(f"""
        Seleciona el numero de la categoria
        """)
        else:
            break
    
    while True:
        try:
            nombre_plato =  input("""
        Ingresa el nombre del plato

        => """)
        except:
            pass
        else:
            break

    try:
        cursor.execute(f"INSERT INTO plato VALUES (null,'{nombre_plato}', {opcion_categoria})")
    except sqlite3.IntegrityError:
        print(f"""
    El plato {nombre_plato} ya existe
    """)
    else:
        print(f"""
    Se ha creado con exito el plato {nombre_plato}
    """)

    conexion.commit()
    conexion.close()


def mostrar_menu():
    conexion = sqlite3.connect('restaurante.db')
    cursor =  conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()

    for categoria in categorias:
        print(f"""
    -----{categoria[1]}-----""")
        platos = cursor.execute(f"SELECT * FROM plato WHERE categoria_id={categoria[0]}").fetchall()
        for plato in platos:
            print(f"""    {plato[1]}""")
        

    conexion.close()

crear_db()

while True:
    print("\n----------------BIENVENIDO A MENU DE CREACION (RESTAURANTE)----------------")

    opcion =  input("""
    Opciones:

    [1] Agregar Categoria
    [2] Agregar Plato
    [3] Mostrar Menu
    [4] Salir
    
    => """)

    if opcion ==  "1":
        agregar_categoria()

    elif opcion == "2":
        agregar_plato()

    elif opcion == "3":
        mostrar_menu()

    elif opcion == "4":
        print("""
    Hasta la proxima..... ˋωˊ 
    """)
        break

    else:
        print("Ingresa una nuevamente la opcion")


