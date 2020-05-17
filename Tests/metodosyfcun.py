def imprimirLista(lista_test):
    '''
    DOCSTRING: Informacion acerca de la funcion
    INPUT: una lista
    OUTPUT: Agrega el valor 5 en la posicion 3 de la lista
    '''
    print(lista1)
    print('________________________')
    lista1.insert(3,5)
    print(lista1) 

lista1 = [1,2,3]
imprimirLista(lista1)

def suma(a,b) :
    return a+b

hola = suma(22,337)
print(hola)

def saludo(name='NOMBRE_'): #se asigna un valor por defecto al parametro, 
    #en caso de que no se lo pase el invocar tomara ese valor
    print('Hola ' + name)
saludo()


def check_dog(mystring):
    return 'dog' in mystring.lower()
print(check_dog('Hola esto es una prueba sidogo esta en el string'))


def porcentage(*args): #utiliza un * para N argumentos
    return sum(args)*0.05 #en este caso calcula el %5 de la suma de todos
    #python transforma la entrada en una tupla

porcentage(2,43,5,6,4,3)

def funkwargs(**kwargs): #con ** python convierte el parametro en un diccionario
    if 'fruits' in kwargs:
        print(f'the fruit is: {kwargs["fruits"]}')
    else:
        print('the fruit isnt here')

funkwargs(fruits='Melon')


def myfunc(*args, **kwargs):
    #probando la suma de los dos *args y **kwargs
#cuando se utilicen los dos al mismo tiempo
#siempre va args primero y luego kwargs
    print(args)
    print(kwargs)
    print(f'i would like {args[0]} {kwargs["fruits"]}')

myfunc(1,2,3,4,fruits='Melon', food='Pan', drink='wine')

def listapares(*args):
    return [x for x in args  if x%2==0]

listapares(1,2,3,4,5)

def transfString(mystring):
    mystringdiv = [x for x in mystring]
    mystringOut=''
    y=1
    for x in mystringdiv:
        if y==1:
            mystringOut = mystringOut + x.lower()
            y-=1
        else:
            mystringOut = mystringOut + x.upper()
            y+=1
    
    return mystringOut

transfString('Hola')
