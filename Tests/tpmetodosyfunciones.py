import math
import string

def ej1(rad):
    pi = math.pi
    return (4/3) * (pi) * (rad**3)

print(ej1(2)) 


def ej2(num, low, high):
    return high > num > low 

#Cuenta las mayusculas y Minusculas de una frase
def ej3(mystring):
    n_upper =0
    n_lower =0
    for x in range(0, len(mystring)):
        if mystring[x].isupper():
            n_upper += 1
        elif mystring[x].islower():
            n_lower += 1
    
    print('The number of upper is ' + str(n_upper) + ', the lower number of letters is' + str(n_lower))

ej3('Buenas Tardes señor Ignacio')

#Sacar los repetidos
def ej4(lista):
    retLista = set(lista)
    return list(retLista)

print(ej4([1,2,3,4,5,3,3,3,3,9]))

#**Write a Python function to multiply all the numbers in a list.**
def ej5(listanum):
    result=0
    for x in listanum:
        result *= x
    return result


#**Write a Python function that checks whether a passed in string is palindrome or not.**
def palindromo(texto):
    entero=len(texto)
    if len(texto)%2==0:
        mitad = int(len(texto)/2)
        secondpart = texto[mitad:entero]
    else:
        mitad = int(len(texto)/2) + 1
        secondpart = texto[mitad-1:entero]
        
    firstpart = texto[:mitad]

    secondpartrev = list(secondpart)
    secondpartrev.reverse()
    secondpartrev = ''.join(secondpartrev)

    return firstpart==secondpartrev


palindromo("palindromo")


#**Write a Python function to check whether a string is pangram or not.**
import string
def isPangram(texto, alphabet):
    texto = texto.lower()
    texto = texto.replace(' ','')
    band = True
    alphabet = list(alphabet)
    alpha_dict = {letter:idx for idx, letter in enumerate(alphabet)}
    for x in texto:
        if x in alphabet:
            nro_index = alpha_dict[x]
            alphabet[nro_index] = 0

    #controlo que el alfabeto solo contenga numeros
    for x in alphabet:
        if isinstance(x, int):
            band=True
        else:
            band=False
            break

    return band

isPangram("The quick brown fox jumps over the lazy dog", string.ascii_lowercase)
