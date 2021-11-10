# Utilizando dos funciones anónimas anidadas en una sola línea , debes: 

# Mapear una lista llamada numeros  de la cuál no conoces su contenido y dividir sus valores entre 2.
# A su vez debes filtrar el resultado de esa lista mapeada y eliminar los números que no sean múltiples de 5.

numeros = "dato_pasado"

numeros = list(filter(lambda numero: numero%5 == 0,map(lambda numero: numero/2,numeros)))