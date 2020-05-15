f = open("../Complete-Python-3-Bootcamp/00-Python Object and Data Structure Basics/test.txt", "rt")
print(f.read())
f.close()


fw = open("archivodeTexto.txt", "wt")
fw.write("Hola Mundo!")
fw.close()