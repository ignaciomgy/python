
class Auto():

    tipo = '3 ruedas'
    
    def __init__(self, p1, p2):
        self.nombre = p1
        self.color = p2

    def tocarBocina(self):
        print(f'BEEEEEEEPPPPPPPPPP soy un {self.nombre}')



auto1 = Auto('Ford', 'Rojo')
print(auto1.color)
print(auto1.tipo)
auto1.tocarBocina()