"""letters = 'abcdef'

# the enumerate return a tuple of each string or object with the index
for index, letrs in enumerate(letters) :
    print(str(index) + '--' + letrs + '\n')


# function zip, merge two lists and return tuples with the elements.
mylist1 = [1,2,3,4,5,6,7]
mylist2 = ['a' ,'b', 'c', 'd', 'e']
mylist3 = [100,200,300]

for item in zip(mylist1, mylist2, mylist3) :
    print(item)

lista_unica = list(zip(mylist2,mylist3))
print(lista_unica)

#function IN, check if the item exist in the list and return a boolean 
print('x' in ['a', 'b', 'x'])

#math functions as min, max, random
from random import shuffle
"""

#list comprehencion
frase = "Hola Mundo"
#print(list(frase))
lista_frase = [letra for letra in frase]
#print(lista_frase)
#it can be used to make a list of number ie
numeros = [num**2 for num in range(0,11)]
print(numeros)

#numeros pares ir
numeros = [num for num in range(0,11) if num%2 == 0]
print(numeros)

#se utiliza para completar otras listas con formulas ie
celcius = [10, 20, 30, 40.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

#if else todo en una linea (no recomendable)
numeros_pares = [x for x in range(0,11) if x%2==0 ]
numeros_pares = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(numeros_pares)

#**Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**
['FizzBuzz' if (x%3==0 and x%5==0) else 'Fizz' if x%3==0 else 'Buzz' if x%5==0 else x for x in range(0,101)]
