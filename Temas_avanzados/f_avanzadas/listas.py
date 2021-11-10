# Utiliza todo lo que sabes para
# generar una lista
# en una única línea llamada multiples
# que contenga todos los números múltiples comunes de 2, 3, 4 y 8 entre 0 y 500 (ambos incluidos).
# No puede contener números repetidos y estos deben estar ordenados de menor a mayor.


multiples = [numero for numero in range(0,501) if numero % 2 == 0 and numero%3 == 0 and numero%4 == 0 and numero%8 == 0 ]

print(multiples)




