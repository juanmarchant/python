# Utilizando como base el ejercicio de los personajes que hicimos, en este ejercicio tendrás que crear un gestor de personajes (gestor.py) para añadir y borrar 
# la información de los siguientes personajes:

# |           | Vida | Ataque | Defensa | Alcance |
# |-----------|------|--------|---------|---------|
# | Caballero | 4    | 2      | 4       | 2       |
# | Guerrero  | 2    | 4      | 2       | 4       |
# | Arquero   | 2    | 4      | 1       | 8       |

# Deberás hacer uso del módulo pickle y todos los cambios que realices se irán guardando en un fichero binario personajes.pckl, 
# por lo que aunque cerremos el programa los datos persistirán.**# Crea dos clases, una **Personaje** y otra **Gestor**.

# La clase **Personaje** deberá permitir crear un personaje con el nombre (que será la clase), y sus propiedades de vida, ataque, defensa y alcance 

# Por otro lado la clase **Gestor** deberá incorporar todos los métodos necesarios para **añadir personajes, mostrarlos y borrarlos (a partir de su nombre por ejemplo)** 
# (tendrás que pensar una forma de hacerlo), además de los métodos esenciales para guardar los cambios en el fichero personajes.pckl que se deberían ejecutar automáticamente. 

# En caso de que el personaje ya exista en el Gestor entonces no se creará.#  Una vez lo tengas listo realiza las siguientes prueba en tu código: **

# Crea los tres personajes de la tabla anterior y añádelos al Gestor.

# Muestra los personajes del Gestor.

# Borra al Arquero.

# Muestra de nuevo el Gestor.

from io import open
import pickle


class Personaje():

    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre  = nombre
        self.vida    = vida
        self.ataque  = ataque
        self.defensa = defensa
        self.alcance  = alcance

    def __str__(self):
        return(f"""
        # |           | Vida | Ataque | Defensa | Alcance |
        # |-----------|------|--------|---------|---------|
        # | {self.nombre} | {self.vida}    | {self.ataque}      | {self.defensa}       | {self.alcance}       |
        """)


class Gestor:

    personajes = []

    def __init__(self):
        self.cargar()
    
    def agregar(self, personaje):

        for personajeTemp in self.personajes:
            if personajeTemp.nombre ==  personaje.nombre:
                print(f"Este personaje ya existe => {personaje.nombre}")
                return 

        self.personajes.append(personaje)
        self.guardar()

    def mostrar(self):
        if len(self.personajes) == 0:
            print("No existen personajes aun")
        else:
            for personaje in self.personajes:
                print(personaje)
    
    def borrar(self, personaje):
        for personajeTemp in self.personajes:
            if personajeTemp.nombre ==  personaje:
                self.personajes.remove(personajeTemp)           


    def guardar(self):
        fichero = open('personajes.pckl', 'wb')
        pickle.dump(self.personajes, fichero)
        fichero.close()
        del(fichero)

    def cargar(self):
        fichero = open('personajes.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            # Si el fichero esta vacio
            pass
        finally:    
            fichero.close()
            print(f"Se han cargado {len(self.personajes)} personajes")

G = Gestor()

# G.agregar(Personaje("Caballero",4,2,4,2))
# G.agregar(Personaje("Guerrero",2,4,2,4))
# G.agregar(Personaje("Arquero",2,4,1,8))


G.borrar("Arquero")
G.mostrar()


  