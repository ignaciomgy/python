#MAP mapea una funcion definida sobre un conjunto de objetos
#FILTER aplica en una funcion sobre un conjunto y los filtra por la funcion aplicada

#ej defino las funciones a mapear y filtrar
def cuadrado(a):
    return a**2

def pares(a):
    return a%2==0

numeros = [1,2,3,4,5,6]
#pongo dentro de una lista el resultado para visualizarlo
#mapeo el cuadrado de cada elemento
list(map(cuadrado, numeros))

#filtro por numeros pares
list(filter(pares, numeros))

#LAMBDA es una expresion para definir una sola vez una funcion sin nombres
#EJ
list(map(lambda num:num**2, [1,2,3,4,5]))
list(filter(lambda a:a%2==0, [1,2,3,4,5,6]))

list(map(lambda a:a[0], ['Juan', 'Paco', 'Pedro']))

#Reverse de cada string en la lista
list(map(lambda a:a[::-1], ['Juan', 'Paco', 'Pedro']))

