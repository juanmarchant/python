# Crea una función generadora llamada cuadrados(numero)
# que a partir de un número genere todos los números de 1 a X (ambos incluidos) y sus potencias de dos.

def cuadrados(extension):
    for numero in range(1,extension+1):
        yield numero, numero**2

print([numero for numero in cuadrados(5)])