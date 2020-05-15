# \n Salto de linea
# \t TAb
# Con strings myString[inicio:fin:paso].
myString = "hola como estas, que tal estuvo el asado"
#print(myString[::-1])
#en valores negativos el indice lo toma desde el final hacia el inicio
#print("tinker"[1:4])

#result = 100 / 88
#print("El resultado es {r:1.3f}".format(r=result))
#otra forma
#print(f"El resultado es {result:1.3f}")

#ordenamiento de listas SORT
una_lista = ["a", "b", "e", "x", "c"]
una_lista.sort()
#print(una_lista)

#para diccionarios
d = {"naranjas":100, "pomelos":300, "sandia":900}
print(d.keys())
print(d.values())
print(d.items())

#tuplas
print("------------- tuplas --------------------")
t = ('a', 'a', 'b')
print(t.count('a'))
print(t.index('a'))
print(set([1,1,2,3]))